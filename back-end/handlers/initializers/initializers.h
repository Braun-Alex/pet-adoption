#pragma once

#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPServerRequest.h"
#include "Poco/Net/HTTPServerResponse.h"
#include "Poco/Util/ServerApplication.h"
#include <Poco/Crypto/DigestEngine.h>
#include <Poco/Crypto/CryptoStream.h>
#include "Poco/Data/PostgreSQL/Connector.h"
#include "Poco/Data/Session.h"
#include "Poco/Data/SessionPool.h"
#include <Poco/Util/PropertyFileConfiguration.h>
#include <Poco/SingletonHolder.h>

using namespace Poco::Net;
using namespace Poco::Data;

const int SALT_SIZE = 32,
          MAX_SERVER_REQUEST_QUEUE_SIZE = 100,
          MAX_SERVER_THREAD_POOL_SIZE = 16;

const std::string CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

std::string hashData(const std::string& data);

void setHeaderResponse(HTTPServerResponse& response);

bool connectedToDatabase();

class SessionPoolManager {
public:
    static void setConfigPath(const std::string& path);
    SessionPoolManager();
    Poco::Data::SessionPool& getPool();

private:
    static std::string _configPath;
    std::unique_ptr<Poco::Data::SessionPool> _pool;

    static std::unique_ptr<Poco::Data::SessionPool> initPool(const std::string& configPath);

    friend class Poco::SingletonHolder<SessionPoolManager>;
};

SessionPoolManager& getSessionPoolManager();