#include <userService/UserService.hpp>


UserService::UserService(/* args */): pUserController_(new UserController())
{
    std::cout<<__FUNCTION__<<": UserService constructor. pUserController_ == nullptr: " << if(pUserController_) << "\n";
}

UserService::~UserService()
{
}

HTTPRequestHandler* UserService::registerUser(HTTPServerRequest& request, HTTPServerResponse& response){
    Application& app = Application::instance();
    const std::string& clientAddress = request.clientAddress().toString();
    app.logger().information("Request \"Sign up user\" from %s", clientAddress);

    setHeaderResponse(response);
    response.setContentType("text/html");

    HTMLForm form(request, request.stream());
    auto userEmail = form.find("user-email");
    auto userPassword = form.find("user-password");
    std::cout<<___FUNCTION__<<": UserService::registerUser called." << " userEmail: " << userEmail<<" userPassword: "<< userPassword<<"\n";
    pUserController_->registerUser(user);

    return nullptr;
}

HTTPRequestHandler* UserService::authorizeUser(HTTPServerRequest& request, HTTPServerResponse& response){
    std::cout<<___FUNCTION__<<": UserService::authorizeUser called.";
    pUserController_->authorizeUser(user);
    
    return nullptr;
}
