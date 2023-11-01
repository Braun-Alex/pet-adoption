#include "requestHandler.hpp"

#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPServerRequest.h"


RequestHandler::RequestHandler():pUserService_(new UserService()){
    handlers["/user/register"] = [this](/*const HTTPServerRequest& request*/) -> HTTPRequestHandler* {return pUserService_->registerUser(/*request*/); };
    // handlers["/user/register"] = pUserService_->registerUser();
    handlers["/user/authorize"] = [this](/*const HTTPServerRequest& request*/) -> HTTPRequestHandler* {return pUserService_->authorizeUser(/*request*/); };

}

void RequestHandler::handleRequest(HTTPServerRequest& request,
                                               HTTPServerResponse& response) {

     auto handler = handlers.find(request.getURI());
        if (handler != handlers.end()) {
            handler->second();
        }
}