#pragma once

#include "local-structs/localStructs.hpp"
#include "Poco/Net/HTTPRequestHandler.hpp"
#include "Poco/Net/HTMLForm.h"

class UserServiceInterface{
    public:
        virtual HTTPRequestHandler* registerUser(HTTPServerRequest& request, HTTPServerResponse& response);
        virtual HTTPRequestHandler* authorizeUser(HTTPServerRequest& request, HTTPServerResponse& response);    
};