#pragma once

#include "orm/user/User.h"
#include "initializers/initializers.h"

#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPServerRequest.h"
#include "Poco/Net/HTTPServerResponse.h"
#include "Poco/Util/ServerApplication.h"
#include <Poco/Crypto/DigestEngine.h>
#include <Poco/Crypto/CryptoStream.h>
#include "Poco/Data/PostgreSQL/Connector.h"
#include "Poco/Data/Session.h"
#include "Poco/Net/HTMLForm.h"
#include "Poco/JSON/Object.h"
#include "Poco/ActiveRecord/ActiveRecord.h"

#include <random>

using namespace Poco;
using namespace Poco::Net;
using namespace Poco::Util;

const int SALT_SIZE = 32;
const std::string CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

std::string hashData(const std::string& data);

class PingRequestHandler: public HTTPRequestHandler {
    void handleRequest(HTTPServerRequest& request, HTTPServerResponse& response) override;
};

class RegisterUserRequestHandler: public HTTPRequestHandler {
    void handleRequest(HTTPServerRequest& request, HTTPServerResponse& response) override;
};

class AuthorizeUserRequestHandler: public HTTPRequestHandler {
    void handleRequest(HTTPServerRequest& request, HTTPServerResponse& response) override;
};
