#include "registerRequestHandler.hpp"

using namespace Poco::Net;
using namespace Poco::Util;
using namespace DatabaseSystem;

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
        RegistrationService service(userEmail->second, userPassword->second);
        if (service.registerUser()) {
            response.setStatus(HTTPResponse::HTTP_OK);
        } else {
            response.setStatus(HTTPResponse::HTTP_CONFLICT);
        }
    }

    response.send();
}