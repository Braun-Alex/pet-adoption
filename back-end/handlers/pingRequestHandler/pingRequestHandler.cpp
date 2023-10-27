#include "pingRequestHandler.h"
#include "../../services/tokenService/tokenService.h"

#include "Poco/JWT/Token.h"
#include "Poco/JWT/Serializer.h"

using namespace Poco::Net;
using namespace Poco::Util;
using namespace Poco;

void PingRequestHandler::handleRequest(HTTPServerRequest& request,
                                       HTTPServerResponse& response) {
    try {
        Application &app = Application::instance();
        const std::string &clientAddress = request.clientAddress().toString();
        app.logger().information("Request \"Ping server\" from %s", clientAddress);

        setHeaderResponse(response);
        response.setContentType("application/json");

        Poco::JSON::Object result;
        result.set("Your IP address", clientAddress);
        result.set("Your URI", request.getURI());
        result.set("Private key", KeyManager::getPrivateKeyPath());
        result.set("Public key", KeyManager::getPublicKeyPath());
        std::string accessToken = TokenService::generateAccessToken("lamanasakasa@gmail.com");
        result.set("Access token", accessToken);
        std::string refreshToken = TokenService::generateRefreshToken("lamanasakasa@gmail.com");
        result.set("Refresh token", refreshToken);
        result.set("Verifying access token", TokenService::verifyToken(accessToken));
        result.set("Verifying refresh token", TokenService::verifyToken(refreshToken));

        std::ostream &answer = response.send();
        result.stringify(answer);
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
    }
}