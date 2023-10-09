#include "pingRequestHandler.h"

using namespace Poco;
using namespace Poco::Net;
using namespace Poco::Util;
using namespace Poco::Data;
using namespace Poco::Data::Keywords;
using namespace DatabaseSystem;
using Poco::Data::Session;
using Poco::Data::Statement;
using Poco::ActiveRecord::Context;

std::string hashData(const std::string& data) {
    Poco::Crypto::DigestEngine engine("SHA256");
    engine.update(data);
    return Crypto::DigestEngine::digestToHex(engine.digest());
}

void PingRequestHandler::handleRequest(HTTPServerRequest& request,
                                       HTTPServerResponse& response) {
    Application& app = Application::instance();
    const std::string& clientAddress = request.clientAddress().toString();
    app.logger().information("Request \"Ping server\" from %s", clientAddress);

    setHeaderResponse(response);
    response.setContentType("application/json");

    Poco::JSON::Object result;
    result.set("Your IP address", clientAddress);
    result.set("Your URI", request.getURI());

    std::ostream& answer = response.send();
    result.stringify(answer);
}

void RegisterUserRequestHandler::handleRequest(HTTPServerRequest& request,
                                       HTTPServerResponse& response) {
    Application& app = Application::instance();
    const std::string& clientAddress = request.clientAddress().toString();
    app.logger().information("Request \"Sign up user\" from %s", clientAddress);

    setHeaderResponse(response);
    response.setContentType("text/html");

    HTMLForm form(request, request.stream());
    auto userEmail = form.find("user-email");
    auto userPassword = form.find("user-password");

    if (userEmail == form.end() || userPassword == form.end()) {
        response.setStatus(HTTPResponse::HTTP_BAD_REQUEST);
    } else {
        Poco::Data::Session session = getSessionPoolManager().getPool().get();
        Context::Ptr pContext = new Context(session);
        User::Ptr pUser = User::find(pContext, hashData(userEmail->second));
        if (pUser) {
            response.setStatus(HTTPResponse::HTTP_CONFLICT);
        } else {
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_int_distribution<> dist(0, 255);
            std::string salt;
            salt.reserve(SALT_SIZE);
            for (size_t i = 0; i < SALT_SIZE; ++i) {
                salt += CHARSET[dist(gen) % CHARSET.size()];
            }
            pUser = new User(hashData(userEmail->second));
            pUser->password(hashData(userPassword->second + salt));
            pUser->salt(salt);
            pUser->create(pContext);
            response.setStatus(HTTPResponse::HTTP_OK);
        }
    }

    response.send();
}

void AuthorizeUserRequestHandler::handleRequest(HTTPServerRequest& request,
                                               HTTPServerResponse& response) {
    Application& app = Application::instance();
    const std::string& clientAddress = request.clientAddress().toString();
    app.logger().information("Request \"Sign in user\" from %s", clientAddress);

    setHeaderResponse(response);
    response.setContentType("text/html");

    HTMLForm form(request, request.stream());
    auto userEmail = form.find("user-email");
    auto userPassword = form.find("user-password");

    if (userEmail == form.end() || userPassword == form.end()) {
        response.setStatus(HTTPResponse::HTTP_BAD_REQUEST);
    } else {
        Poco::Data::Session session = getSessionPoolManager().getPool().get();
        Context::Ptr pContext = new Context(session);
        User::Ptr pUser = User::find(pContext, hashData(userEmail->second));
        if (!pUser) {
            response.setStatus(HTTPResponse::HTTP_UNAUTHORIZED);
        } else {
            if (pUser->password() == hashData(userPassword->second + pUser->salt())) {
                response.setStatus(HTTPResponse::HTTP_OK);
            } else {
                response.setStatus(HTTPResponse::HTTP_UNAUTHORIZED);
            }
        }
    }

    response.send();
}