cmake_minimum_required(VERSION 3.26)
project(server)

set(CMAKE_CXX_STANDARD 23)
set(HEADERS handlers/pingRequestHandler/pingRequestHandler.h
        handlers/registerRequestHandler/registerRequestHandler.h
        handlers/authorizeRequestHandler/authorizeRequestHandler.h
        services/registrationService/registrationService.h
        services/authService/authService.h
        services/tokenService/tokenService.h
        services/cipherService/cipherService.h
        orm/animal/Animal.h
        orm/user/User.h
        orm/shelter/Shelter.h
        orm/emailVerification/EmailVerification.h
        orm/phoneVerification/PhoneVerification.h
        initializers/initializers.h

        local-structs/localStructs.hpp
        interfaces/UserControllerInterface.hpp
        interfaces/UserServiceInterface.hpp
        controllesrs/UserController.hpp
        services/userServices/UserService.hpp


)
set(SOURCES handlers/pingRequestHandler/pingRequestHandler.cpp
        handlers/registerRequestHandler/registerRequestHandler.cpp
        handlers/authorizeRequestHandler/authorizeRequestHandler.cpp
        services/registrationService/registrationService.cpp
        services/authService/authService.cpp
        services/tokenService/tokenService.cpp
        services/cipherService/cipherService.cpp

        services/userServices/UserService.cpp
        controllesrs/UserController.cpp

        orm/animal/Animal.cpp
        orm/user/User.cpp
        orm/shelter/Shelter.cpp
        orm/emailVerification/EmailVerification.cpp
        orm/phoneVerification/PhoneVerification.cpp
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

target_include_directories(
        server
        PUBLIC
        ${CMAKE_SOURCE_DIR}/local-structs
        ${CMAKE_SOURCE_DIR}/interfaces
        ${CMAKE_SOURCE_DIR}/controllers
        ${CMAKE_SOURCE_DIR}/initializers
        ${CMAKE_SOURCE_DIR}/services/userService

)

target_link_libraries(${PROJECT_NAME} PUBLIC Foundation Crypto Net NetSSL JWT Util
        JSON ActiveRecord DataPostgreSQL)
