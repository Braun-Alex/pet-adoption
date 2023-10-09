#include "initializers.h"

using namespace Poco::Net;
using namespace Poco::Data;
using namespace Poco::Data::Keywords;

void setHeaderResponse(HTTPServerResponse& response) {
    response.setChunkedTransferEncoding(true);
    response.setKeepAlive(true);
    response.set("access-control-allow-origin", "*");
}

bool connectedToDatabase() {
    Session session = getSessionPoolManager().getPool().get();
    try {
        std::size_t result = 0;
        session << "SELECT 3", into(result), now;
        return result == 3;
    } catch (const Poco::Exception&) {
        return false;
    }
}


void SessionPoolManager::setConfigPath(const std::string& path) {
    _configPath = path;
}

SessionPoolManager::SessionPoolManager(): _pool(initPool(_configPath)) {}

SessionPool& SessionPoolManager::getPool() {
    return *_pool;
}

std::string SessionPoolManager::_configPath;

std::unique_ptr<Poco::Data::SessionPool> SessionPoolManager::initPool(const std::string& configPath) {
    Poco::AutoPtr<Poco::Util::PropertyFileConfiguration> pConf(
            new Poco::Util::PropertyFileConfiguration(configPath));
    std::string connectionData = "host=" + pConf->getString("host") +
                                 " port=" + std::to_string(pConf->getInt("port")) +
                                 " user=" + pConf->getString("user") +
                                 " password=" + pConf->getString("password") +
                                 " dbname=" + pConf->getString("databaseName");
    PostgreSQL::Connector::registerConnector();
    return std::make_unique<Poco::Data::SessionPool>(PostgreSQL::Connector::KEY, connectionData);
}

SessionPoolManager& getSessionPoolManager() {
    static Poco::SingletonHolder<SessionPoolManager> sh;
    return *sh.get();
}