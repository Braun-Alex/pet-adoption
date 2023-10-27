#pragma once

#include "../../initializers/initializers.h"

#include "Poco/JWT/Signer.h"
#include "Poco/JWT/Token.h"

constexpr int ACCESS_TOKEN_EXPIRATION = 15 * 60;
constexpr int REFRESH_TOKEN_EXPIRATION = 30 * 24 * 60 * 60;

#include <string>

using namespace Poco;

class TokenService {
public:
    TokenService() = default;
    static std::string generateAccessToken(const std::string& id);
    static std::string generateRefreshToken(const std::string& id);

    static bool verifyToken(const std::string& signedToken);

private:
    static JWT::Token getToken(const std::string& id, int expiration);
    static std::string signToken(JWT::Token& unsignedToken);
};