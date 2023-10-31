#pragma once
#include <memory>

#include <interfaces/UserServiceInterface.h>
//#include <interfaces/UserControllerInterface.h>
#include <controllers/UserController.h>

class UserService: UserServiceInterface
{
private:
    std::unique_ptr<UserControllerInterface> pUserController_;
    
public:
    UserService(/* args */);
    ~UserService();
};


