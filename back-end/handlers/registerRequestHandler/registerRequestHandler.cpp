#include "registerRequestHandler.h"

using namespace Poco::Net;
using namespace Poco::Util;
using namespace Poco::Data::Keywords;
using namespace DatabaseSystem;
using Poco::ActiveRecord::Context;

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