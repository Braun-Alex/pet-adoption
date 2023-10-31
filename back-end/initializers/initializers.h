#pragma once

#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPServerRequest.h"
#include "Poco/Net/HTTPServerResponse.h"
#include "Poco/Util/ServerApplication.h"
#include "Poco/Crypto/DigestEngine.h"
#include "Poco/Crypto/CryptoStream.h"
#include "Poco/Crypto/ECKey.h"
#include "Poco/Data/PostgreSQL/Connector.h"
#include "Poco/Data/Session.h"
#include "Poco/Data/SessionPool.h"
#include "Poco/JSON/Object.h"
#include "Poco/Util/PropertyFileConfiguration.h"
#include "Poco/SingletonHolder.h"
#include "Poco/FileStream.h"

#include <thread>
#include <random>

using namespace Poco::Net;
using namespace Poco::Data;

const int SALT_LENGTH = 32,
          MAX_SERVER_REQUEST_QUEUE_SIZE = 300;

const std::string CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

std::string hashData(const std::string& data);

std::string generateSalt(size_t length);

void setHeaderResponse(HTTPServerResponse& response);

bool connectedToDatabase();

class SessionPoolManager {
public:
    SessionPoolManager();
    static void setConfigPath(const std::string& path);
    Poco::Data::SessionPool& getPool();

private:
    static std::string _configPath;
    std::unique_ptr<Poco::Data::SessionPool> _pool;

    static std::unique_ptr<Poco::Data::SessionPool> initPool(const std::string& configPath);

    friend class Poco::SingletonHolder<SessionPoolManager>;
};

SessionPoolManager& getSessionPoolManager();

class KeyManager {
public:
    KeyManager();
    static void setPrivateKeyPath(const std::string& privateKeyPath);
    static void setPublicKeyPath(const std::string& publicKeyPath);
    static void setPassphrasePath(const std::string& passphrasePath);

    static const std::string& getPrivateKeyPath();
    static const std::string& getPublicKeyPath();
    [[nodiscard]] const std::string& getPassphrase() const;

private:
    static std::string _privateKeyPath;
    static std::string _publicKeyPath;
    static std::string _passphrasePath;

    static std::string initPassphrase(const std::string& passphrasePath);

    const std::string _passphrase;

    friend class Poco::SingletonHolder<KeyManager>;
};

KeyManager& getKeyManager();