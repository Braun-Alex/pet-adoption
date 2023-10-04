#include "handlers/pingRequestHandler.h"

#include "Poco/Net/HTTPServer.h"
#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPRequestHandlerFactory.h"
#include "Poco/Net/HTTPServerRequest.h"
#include "Poco/Net/HTTPServerResponse.h"
#include "Poco/Util/ServerApplication.h"

using namespace Poco;
using namespace Poco::Net;
using namespace Poco::Util;

class RequestHandlerFactory: public HTTPRequestHandlerFactory {
    HTTPRequestHandler *createRequestHandler(const HTTPServerRequest &request) override {
        return new PingRequestHandler();
    }
};

class WebServerApp: public ServerApplication
{
    void initialize(Application& self) override
    {
        loadConfiguration();
        ServerApplication::initialize(self);
    }

    int main(const std::vector<std::string>&) override
    {
        UInt16 port = static_cast<UInt16>(config().getUInt("port", 8080));
        auto* params = new HTTPServerParams;
        params->setMaxQueued(100);
        params->setMaxThreads(16);
        HTTPServer srv(new RequestHandlerFactory, port, params);
        srv.start();
        logger().information("HTTP Server started on port %hu.", port);
        waitForTerminationRequest();
        logger().information("Stopping HTTP Server...");
        srv.stop();

        return Application::EXIT_OK;
    }
};

POCO_SERVER_MAIN(WebServerApp)
