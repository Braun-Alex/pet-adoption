#pragma once
#include <memory>

#include "interfaces/UserServiceInterface.hpp"
//#include <interfaces/UserControllerInterface.h>
#include "controllers/UserController.hpp"

class UserService: UserServiceInterface
{
private:
    std::unique_ptr<UserControllerInterface> pUserController_;
    
public:
    UserService(/* args */);
    ~UserService();
};


