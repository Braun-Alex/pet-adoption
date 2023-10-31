#include <controllers/UserController.h>
#include <initializers/initializers.h>


UserController::UserController(/*const Poco::Data::Session session, Context::Ptr pContext*/){
    std::cout<<__FUNXTION__<<": UserController constructor called\n";
    Poco::Data::Session session = getSessionPoolManager().getPool().get();
    session_ = session;
    context_ = new Context(session);
}

UserController::registerUser(const LocalStructs::User& user){
    std::cout<<__FUNCTION__<<"UserController::registerUser called.\n";
}

UserController::authorizeUser(const LocalStructs::User& user){
    std::cout<<__FUNCTION__<<"UserController::authorizeUser called.\n";
}

