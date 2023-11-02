#include "requestHandler.hpp"

#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPServerRequest.h"
#include "initializers/initializers.h"

using namespace Poco::Util;


RequestHandler::RequestHandler():pUserService_(new UserService()){
     Application& app = Application::instance();
    app.logger().information("RequestHandle");
    handlers_["/user/register"] = [this](HTTPServerRequest& request, HTTPServerResponse& response) -> void
                                    {pUserService_->registerUser(request, response); };
    // handlers["/user/register"] = pUserService_->registerUser();
    handlers_["/user/authorize"] = [this](HTTPServerRequest& request, HTTPServerResponse& response) -> void {return pUserService_->authorizeUser(request, response); };
    app.logger().information("handlers are initialized");

}

void RequestHandler::handleRequest(HTTPServerRequest& request,
                                               HTTPServerResponse& response) {

    Application& app = Application::instance();
    app.logger().information("RequestHandle: RequestHandler::handleRequest called");
    app.logger().information("RequestHandle %s", request.getURI());

    try{
        auto handler = handlers_.find(request.getURI());
        request.
        if (handler != handlers_.end()) {
            app.logger().information("server know about this request:  %s", request.getURI());
            handler->second(request, response);
        }
        else{
                app.logger().information("server doesn't know about this request:  %s", request.getURI());
                response.setContentType("text/html");

                response.setStatus(HTTPResponse::HTTP_BAD_REQUEST);
                response.send();
                //response.end();
                
        }
    }
    catch(...){
        app.logger().information("Eror")
        // std::exception_ptr p = std::current_exception();
        // app.logger().information("Error: %v", p.)
    }

     

}