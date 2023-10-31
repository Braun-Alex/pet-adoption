#pragma once

#include "loca-structs/localStructs.h"
#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTMLForm.h"

class UserServiceInterface{
    public:
        virtual HTTPRequestHandler* registerUser(HTTPServerRequest& request, HTTPServerResponse& response);
        virtual HTTPRequestHandler* authorizeUser(HTTPServerRequest& request, HTTPServerResponse& response);    
};