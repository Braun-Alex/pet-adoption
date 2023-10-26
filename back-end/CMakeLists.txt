cmake_minimum_required(VERSION 3.26)
project(server)

set(CMAKE_CXX_STANDARD 23)
set(HEADERS handlers/pingRequestHandler/pingRequestHandler.h
        handlers/registerRequestHandler/registerRequestHandler.h
        handlers/authorizeRequestHandler/authorizeRequestHandler.h
        services/registrationService/registrationService.h
        services/authService/authService.h
        orm/user/User.h
        initializers/initializers.h
)
set(SOURCES handlers/pingRequestHandler/pingRequestHandler.cpp
        handlers/registerRequestHandler/registerRequestHandler.cpp
        handlers/authorizeRequestHandler/authorizeRequestHandler.cpp
        services/registrationService/registrationService.cpp
        services/authService/authService.cpp
        orm/user/User.cpp
        initializers/initializers.cpp
        main.cpp
)

include(FetchContent)
FetchContent_Declare(
        Poco
        URL https://github.com/pocoproject/poco/archive/refs/tags/poco-1.12.4-release.zip
)
FetchContent_MakeAvailable(Poco)

add_executable(${PROJECT_NAME} ${HEADERS} ${SOURCES})

target_link_libraries(${PROJECT_NAME} PUBLIC Foundation Crypto Net NetSSL Util
        JSON ActiveRecord DataPostgreSQL)
