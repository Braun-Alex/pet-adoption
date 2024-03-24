#include "initializers.h"

using namespace Poco;
using namespace Poco::Net;
using namespace Poco::Util;
using namespace Poco::Data;
using namespace Poco::Data::Keywords;

std::string hashData(const std::string& data) {
    Poco::Crypto::DigestEngine engine("SHA256");
    engine.update(data);
    return Crypto::DigestEngine::digestToHex(engine.digest());
}

std::string generateSalt(size_t length) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, 255);
    std::string salt;
    salt.reserve(length);
    for (size_t i = 0; i < length; ++i) {
        salt += CHARSET[dist(gen) % CHARSET.size()];
    }
    return salt;
}

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

SessionPoolManager::SessionPoolManager(): _pool(initPool(_configPath)) {}

void SessionPoolManager::setConfigPath(const std::string& path) {
    _configPath = path;
}

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

KeyManager::KeyManager(): _passphrase(initPassphrase(_passphrasePath)) {}

void KeyManager::setPrivateKeyPath(const std::string& privateKeyPath) {
    _privateKeyPath = privateKeyPath;
}

void KeyManager::setPublicKeyPath(const std::string& publicKeyPath) {
    _publicKeyPath = publicKeyPath;
}

void KeyManager::setPassphrasePath(const std::string& passphrasePath) {
    _passphrasePath = passphrasePath;
}

const std::string& KeyManager::getPrivateKeyPath() {
    return _privateKeyPath;
}

const std::string& KeyManager::getPublicKeyPath() {
    return _publicKeyPath;
}

const std::string& KeyManager::getPassphrase() const {
    return _passphrase;
}

std::string KeyManager::initPassphrase(const std::string& passphrasePath) {
    try {
        Poco::FileInputStream fis(passphrasePath);
        std::string passphrase;

        while (!fis.eof()) {
            char buffer[256];
            fis.read(buffer, sizeof(buffer));
            passphrase.append(buffer, fis.gcount());
        }

        fis.close();

        return passphrase;
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
        return "";
    }
}

std::string KeyManager::_privateKeyPath;
std::string KeyManager::_publicKeyPath;
std::string KeyManager::_passphrasePath;

KeyManager& getKeyManager() {
    static Poco::SingletonHolder<KeyManager> sh;
    return *sh.get();
}