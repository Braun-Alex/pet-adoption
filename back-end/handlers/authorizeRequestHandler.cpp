#include "authorizeRequestHandler.h"

using namespace Poco::Net;
using namespace Poco::Util;
using namespace Poco::Data::Keywords;
using namespace DatabaseSystem;
using Poco::ActiveRecord::Context;

void AuthorizeUserRequestHandler::handleRequest(HTTPServerRequest& request,
                                                HTTPServerResponse& response) {
    Application &app = Application::instance();
    const std::string &clientAddress = request.clientAddress().toString();
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