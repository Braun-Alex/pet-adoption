#include "authorizeRequestHandler.h"

using namespace Poco;
using namespace Poco::Net;
using namespace Poco::Util;
using namespace Poco::JSON;
using namespace DatabaseSystem;

void AuthorizeUserRequestHandler::handleRequest(HTTPServerRequest& request,
                                                HTTPServerResponse& response) {
    Application& app = Application::instance();
    const std::string &clientAddress = request.clientAddress().toString();
    app.logger().information("Request \"Sign in user\" from %s", clientAddress);

    setHeaderResponse(response);
    response.setContentType("application/json");

    URI uri(request.getURI());
    bool areValidParams = true;
    auto params = uri.getQueryParameters();
    std::map<std::string, std::string> parameters;

    auto contains = [&](const std::string& queryParameter) -> bool {
        for (const auto& [key, value]: params) {
            if (key == queryParameter) {
                parameters[key] = value;
                return true;
            }
        }
        return false;
    };

    for (const auto& queryParameter: queryParams) {
        if (!contains(queryParameter)) {
            response.setStatus(HTTPResponse::HTTP_BAD_REQUEST);
            areValidParams = false;
            break;
        }
    }

    if (areValidParams) {
        std::string userEmail = parameters["userEmail"];
        AuthService service(userEmail, parameters["userPassword"]);
        if (service.authorizeUser()) {
            response.setStatus(HTTPResponse::HTTP_OK);
            Object tokens;
            tokens.set("accessToken", TokenService::generateAccessToken(userEmail));
            tokens.set("refreshToken", TokenService::generateRefreshToken(userEmail));
            std::ostream &answer = response.send();
            tokens.stringify(answer);
            return;
        } else {
            response.setStatus(HTTPResponse::HTTP_UNAUTHORIZED);
        }
    }

    response.send();
}