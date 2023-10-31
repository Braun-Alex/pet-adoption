#pragma once

#include "../../orm/user/User.h"
#include "../../initializers/initializers.h"

class AuthService {
public:
    AuthService(const std::string& email, const std::string& password);
    bool authorizeUser();

private:
    const std::string& _email;
    const std::string& _password;
};