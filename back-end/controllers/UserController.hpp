#pragma once

#include "Poco/ActiveRecord/Context.h"
#include "interfaces/UserControllerInterface.hpp"

using namespace Poco;
using namespace Poco::Data;
//using Poco::ActiveRecord::Context;


class UserController:public UserControllerInterface{
    public:

        UserController(/*const Poco::Data::Session session, Context::Ptr pContext*/);

        bool registerUser(const LocalStructs::User& user) override;
        bool authorizeUser(const LocalStructs::User& user) override;
    private:
        std::shared_ptr<Session> session_;
        Poco::ActiveRecord::Context::Ptr pContext_;

};