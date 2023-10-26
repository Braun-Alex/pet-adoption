#include "authorizeRequestHandler.h"

using namespace Poco::Net;
using namespace Poco::Util;
using namespace DatabaseSystem;

void AuthorizeUserRequestHandler::handleRequest(HTTPServerRequest& request,
                                                HTTPServerResponse& response) {
    Application& app = Application::instance();
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
        AuthService service(userEmail->second, userPassword->second);
        if (service.authorizeUser()) {
            response.setStatus(HTTPResponse::HTTP_OK);
        } else {
            response.setStatus(HTTPResponse::HTTP_UNAUTHORIZED);
        }
    }

    response.send();
}