#include "tokenService.h"

using namespace Poco;
using namespace Poco::Util;

JWT::Token TokenService::getToken(const std::string& id, int expiration) {
    try {
        JWT::Token token;
        token.setType("JWT");
        token.setSubject(CipherService::encrypt(id, getKeyManager().getPassphrase()));
        Timestamp currentTimestamp = Timestamp();
        token.setIssuedAt(currentTimestamp);
        token.setExpiration(currentTimestamp + expiration * Timestamp::resolution());
        return token;
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
        return {};
    }
}

std::string TokenService::generateAccessToken(const std::string& id) {
    try {
        JWT::Token unsignedAccessToken = getToken(id, ACCESS_TOKEN_EXPIRATION);
        return signToken(unsignedAccessToken);
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
        return {};
    }
}

std::string TokenService::generateRefreshToken(const std::string& id) {
    try {
        JWT::Token unsignedRefreshToken = getToken(id, REFRESH_TOKEN_EXPIRATION);
        return signToken(unsignedRefreshToken);
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
        return "";
    }
}

std::string TokenService::signToken(JWT::Token& unsignedToken) {
    JWT::Signer signer(new Crypto::ECKey(KeyManager::getPublicKeyPath(),
                                         KeyManager::getPrivateKeyPath()));
    signer.addAlgorithm("ES256");
    return signer.sign(unsignedToken, JWT::Signer::ALGO_ES256);
}

bool TokenService::verifyToken(const std::string& jwt) {
    JWT::Signer signer(new Crypto::ECKey(KeyManager::getPublicKeyPath(),
                                         KeyManager::getPrivateKeyPath()));
    signer.addAlgorithm("ES256");
    JWT::Token token;
    return signer.tryVerify(jwt, token);
}