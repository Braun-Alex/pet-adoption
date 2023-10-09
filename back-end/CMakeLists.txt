cmake_minimum_required(VERSION 3.26)
project(server)

set(CMAKE_CXX_STANDARD 23)
set(HEADERS handlers/pingRequestHandler.h
            handlers/orm/user/User.h
            handlers/initializers/initializers.h
)
set(SOURCES handlers/pingRequestHandler.cpp main.cpp
            handlers/orm/user/User.cpp
            handlers/initializers/initializers.cpp
)

include(FetchContent)
FetchContent_Declare(
        Poco
        URL https://github.com/pocoproject/poco/archive/refs/tags/poco-1.12.4-release.zip
)
FetchContent_MakeAvailable(Poco)

add_executable(${PROJECT_NAME} ${HEADERS} ${SOURCES})
target_link_libraries(${PROJECT_NAME} PUBLIC Foundation Crypto Net Util
        JSON ActiveRecord DataPostgreSQL)
