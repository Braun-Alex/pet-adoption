#include "registrationService.h"

using namespace Poco;
using namespace Poco::Util;
using namespace DatabaseSystem;
using Poco::ActiveRecord::Context;

RegistrationService::RegistrationService(const std::string& email, const std::string& password): _email(email), _password(password) {}

bool RegistrationService::registerUser() {
    try {
        Poco::Data::Session session = getSessionPoolManager().getPool().get();
        Context::Ptr pContext = new Context(session);
        User::Ptr pUser = User::find(pContext, hashData(_email));
        if (pUser) {
            return false;
        }
        std::string salt = generateSalt(SALT_LENGTH);
        pUser = new User(hashData(_email));
        pUser->hashedPassword(hashData(_password + salt));
        pUser->salt(salt);
        pUser->create(pContext);
        return true;
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
        return false;
    }
}