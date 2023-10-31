#pragma once

#include "../../services/authService/authService.h"
#include "../../services/tokenService/tokenService.h"
#include "../../services/cipherService/cipherService.h"
#include "Poco/URI.h"

#include <map>

const std::vector<std::string> queryParams = {
        "userEmail",
        "userPassword"
};

using namespace Poco::Net;

class AuthorizeUserRequestHandler: public HTTPRequestHandler {
    void handleRequest(HTTPServerRequest& request, HTTPServerResponse& response) override;
};