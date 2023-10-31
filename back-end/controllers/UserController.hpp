#pragma once

#include "interfaces/UserControllerInterface.hpp"

using namespace Poco;
using Poco::ActiveRecord::Context;

class UserController: UserControllerInterface{
    public:

        UserController(const Poco::Data::Session session, Context::Ptr pContext);

        bool registerUser(const LocalStructs::User& user) override;
        bool authorizeUser(const LocalStructs::User& user) override;
    private:
        const Poco::Data::Session session_;
        Context::Ptr pContext_;

}