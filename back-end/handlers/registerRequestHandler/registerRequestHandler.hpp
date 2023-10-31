#pragma once

#include "../../services/registrationService/registrationService.h"
#include "Poco/Net/HTMLForm.h"

using namespace Poco::Net;

class RegisterUserRequestHandler: public HTTPRequestHandler {
    void handleRequest(HTTPServerRequest& request, HTTPServerResponse& response) override;
};