#include "UserController.hpp"
#include "initializers/initializers.h"


UserController::UserController(/*const Poco::Data::Session session, Context::Ptr pContext*/){
    std::cout<<": UserController constructor called\n";
    // Poco::Data::Session session = getSessionPoolManager().getPool().get();
    // session_ = session;

    session_ = std::make_shared<Session>(getSessionPoolManager().getPool().get());;

    pContext_ = new Poco::ActiveRecord::Context(*session_);
}

bool UserController::registerUser(const LocalStructs::User& user){
    std::cout<<"UserController::registerUser called.\n";
    return true;
}

bool UserController::authorizeUser(const LocalStructs::User& user){
    std::cout<<"UserController::authorizeUser called.\n";
    return true;
}


