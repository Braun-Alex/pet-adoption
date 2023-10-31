#include "handlers/pingRequestHandler/pingRequestHandler.h"
#include "handlers/registerRequestHandler/registerRequestHandler.h"
#include "handlers/authorizeRequestHandler/authorizeRequestHandler.h"

#include "Poco/Net/HTTPServer.h"
#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPRequestHandlerFactory.h"
#include "Poco/Net/HTTPServerRequest.h"
#include "Poco/Util/ServerApplication.h"
#include "Poco/Net/SecureServerSocket.h"

#include <unordered_map>

using namespace Poco;
using namespace Poco::Net;
using namespace Poco::Util;

class RequestHandlerFactory: public HTTPRequestHandlerFactory {
public:
    RequestHandlerFactory() {
        handlers["/user/register"] = []() -> HTTPRequestHandler* { return new RegisterUserRequestHandler(); };
        handlers["/user/authorize"] = []() -> HTTPRequestHandler* { return new AuthorizeUserRequestHandler(); };
    }
    HTTPRequestHandler* createRequestHandler(const HTTPServerRequest& request) override {
        auto handler = handlers.find(request.getURI());
        if (handler != handlers.end()) {
            return handler->second();
        }
        return new PingRequestHandler();
    }
private:
    std::unordered_map<std::string, std::function<HTTPRequestHandler*()>> handlers;
};

class WebServerApp: public ServerApplication
{
    void initialize(Application& self) override
    {
        initializeSSL();
        loadConfiguration();
        ServerApplication::initialize(self);
    }

    void uninitialize() override
    {
        uninitializeSSL();
        ServerApplication::uninitialize();
    }

    int main(const std::vector<std::string>&) override
    {
        UInt16 port = static_cast<UInt16>(config().getUInt("port", 8080));

        auto pContext = new Context(
                Context::TLSV1_3_SERVER_USE,
                "key.pem",
                "certificate.pem",
                "",
                Context::VERIFY_ONCE,
                9,
                true
        );

        auto* params = new HTTPServerParams;
        params->setMaxQueued(MAX_SERVER_REQUEST_QUEUE_SIZE);
        params->setMaxThreads(static_cast<int>(std::thread::hardware_concurrency()));

        SessionPoolManager::setConfigPath("config.properties");
        if (!connectedToDatabase()) {
            return Application::EXIT_DATAERR;
        }

        KeyManager::setPrivateKeyPath("serverPrivateKey.pem");
        KeyManager::setPublicKeyPath("serverPublicKey.pem");
        KeyManager::setPassphrasePath("serverPassphrase.key");

        SecureServerSocket svs(port, 64, pContext);
        HTTPServer srv(new RequestHandlerFactory, svs, params);

        srv.start();
        logger().information("HTTPS server started on port %hu.", port);
        waitForTerminationRequest();
        logger().information("Stopping HTTPS server...");
        srv.stop();

        return Application::EXIT_OK;
    }
};

POCO_SERVER_MAIN(WebServerApp)
