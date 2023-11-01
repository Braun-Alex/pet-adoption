#include "Poco/Net/HTMLForm.h"
//#include "interfaces/UserControllerInterface.hpp"
#include "userService/UserService.hpp"

using namespace Poco::Net;

class RequestHandler: public HTTPRequestHandler {
    public:
        RequestHandler();
        void handleRequest(HTTPServerRequest& request, HTTPServerResponse& response) override;
    private:
        std::unique_ptr<UserService> pUserService_;
        std::unordered_map<std::string, std::function<HTTPRequestHandler*(/*const HTTPServerRequest& request*/)>> handlers;


};