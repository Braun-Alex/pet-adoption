#pragma once

#include "../../services/authService/authService.h"
#include "Poco/Net/HTMLForm.h"

using namespace Poco::Net;

class AuthorizeUserRequestHandler: public HTTPRequestHandler {
    void handleRequest(HTTPServerRequest& request, HTTPServerResponse& response) override;
};