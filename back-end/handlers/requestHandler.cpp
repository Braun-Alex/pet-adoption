#include "requestHandler.hpp"

#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPServerRequest.h"


RequestHandler::RequestHandler():pUserService_(new UserService()){
    handlers_["/user/register"] = [this](HTTPServerRequest& request, HTTPServerResponse& response) -> void
                                    {pUserService_->registerUser(request, response); };
    // handlers["/user/register"] = pUserService_->registerUser();
    handlers_["/user/authorize"] = [this](HTTPServerRequest& request, HTTPServerResponse& response) -> void {return pUserService_->authorizeUser(request, response); };

}

void RequestHandler::handleRequest(HTTPServerRequest& request,
                                               HTTPServerResponse& response) {

     auto handler = handlers_.find(request.getURI());
        if (handler != handlers_.end()) {
            handler->second(request, response);
        }
}