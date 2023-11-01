#pragma once

#include "local-structs/localStructs.hpp"
#include "Poco/Net/HTMLForm.h"
#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPServerRequest.h"

using namespace Poco::Net;


class UserServiceInterface{
    public:
        virtual HTTPRequestHandler* registerUser(/*HTTPServerRequest& request, HTTPServerResponse& response*/) = 0;
        virtual HTTPRequestHandler* authorizeUser(/*HTTPServerRequest& request, HTTPServerResponse& response*/) = 0;    
};