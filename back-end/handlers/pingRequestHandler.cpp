#include "pingRequestHandler.h"

using namespace Poco;
using namespace Poco::Net;
using namespace Poco::Util;

void PingRequestHandler::handleRequest(HTTPServerRequest& request,
                                       HTTPServerResponse& response) {
    Application &app = Application::instance();
    const std::string& clientAddress = request.clientAddress().toString();
    app.logger().information("Request \"Ping server\" from %s", clientAddress);

    response.setChunkedTransferEncoding(true);
    response.setContentType("application/json");
    response.setKeepAlive(true);
    response.set("access-control-allow-origin", "*");

    Poco::JSON::Object result;
    result.set("Your IP address", clientAddress);
    result.set("Your URI", request.getURI());

    std::ostream& answer = response.send();
    result.stringify(answer);
}