#pragma once

#include <loca-structs/localStructs.h>



class UserControllerInterface{
    public:
        virtual bool registerUser(const LocalStructs::User& user) = 0;
        virtual bool authorizeUser(const LocalStructs::User& user) = 0;

      //  virtual void getUserFromDB(...);
};