#include "authService.h"

using namespace Poco;
using namespace Poco::Util;
using namespace DatabaseSystem;
using Poco::ActiveRecord::Context;

AuthService::AuthService(const std::string& email, const std::string& password): _email(email), _password(password) {}

bool AuthService::authorizeUser() {
    try {
        Poco::Data::Session session = getSessionPoolManager().getPool().get();
        Context::Ptr pContext = new Context(session);
        User::Ptr pUser = User::find(pContext, hashData(_email));
        if (pUser && pUser->hashedPassword() == hashData(_password + pUser->salt())) {
            return true;
        }
        return false;
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
        return false;
    }
}