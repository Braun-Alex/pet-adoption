#pragma once
#include <memory>

#include "interfaces/UserServiceInterface.hpp"
//#include <interfaces/UserControllerInterface.h>
#include "controllers/UserController.hpp"
#include "Poco/ActiveRecord/Context.h"
#include "Poco/Net/HTMLForm.h"
#include <string>


class UserService: public UserServiceInterface
{
private:
    std::unique_ptr<UserControllerInterface> pUserController_;
    
public:

    void registerUser(const HTTPServerRequest& request, HTTPServerResponse& response) override;
    void authorizeUser(const HTTPServerRequest& request, HTTPServerResponse& response) override;    



    UserService(/* args */);
    ~UserService();
};


