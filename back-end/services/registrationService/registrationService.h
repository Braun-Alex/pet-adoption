#pragma once

#include "../../orm/user/User.h"
#include "../../initializers/initializers.h"

class RegistrationService {
public:
    RegistrationService(const std::string& email, const std::string& password);
    bool registerUser();

private:
    const std::string& _email;
    const std::string& _password;
};