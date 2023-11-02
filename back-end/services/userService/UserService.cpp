#include <iostream>
//#include "interfaces/UserServiceInterface.hpp"
#include "UserService.hpp"
//#include "controllers/UserController.hpp"
#include "initializers/initializers.h"

using namespace Poco;
using namespace Poco::Util;
//using namespace DatabaseSystem;
using Poco::ActiveRecord::Context;


UserService::UserService(/* args */): pUserController_(new UserController)
{
    std::cout<<": UserService constructor. pUserController_ == nullptr: " << (pUserController_) << "\n";
}

UserService::~UserService()
{
}

void UserService::registerUser(const HTTPServerRequest& request, HTTPServerResponse& response){
    // Application& app = Application::instance();
    // const std::string& clientAddress = request.clientAddress().toString();
    // app.logger().information("Request \"Sign up user\" from %s", clientAddress);

   // HTMLForm form(request, request.stream());
    setHeaderResponse(response);
    response.setContentType("text/html");

    // auto userEmail = form.find("user-email");
    // auto userPassword = form.find("user-password");
    std::string userEmail = "aboba";
    std::string userPassword = "aboba";

    LocalStructs::User user = {userEmail, userPassword};

    std::cout<<": UserService::registerUser called." << " userEmail: " << user.email<<" userPassword: "<< user.password<<"\n";

   
    //pUserController_->registerUser(user);
}

void UserService::authorizeUser(const HTTPServerRequest& request, HTTPServerResponse& response){
    std::cout<<": UserService::authorizeUser called.";
    std::string userEmail = "aboba";
    std::string userPassword = "aboba";
    LocalStructs::User user= {userEmail, userPassword};

    pUserController_->authorizeUser(user);
}
