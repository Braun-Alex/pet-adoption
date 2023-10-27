#include "../../initializers/initializers.h"

#include "cipherService.h"

using namespace Poco;
using namespace Poco::Crypto;
using namespace Poco::Util;

std::string CipherService::encrypt(const std::string& data, const std::string& passphrase) {
    try {
        std::string initializationVector = generateSalt(INITIALIZATION_VECTOR_LENGTH);
        CipherKey key(AES_MODE, passphrase, initializationVector);
        Cipher::Ptr cipher = CipherFactory::defaultFactory().createCipher(key);
        return encode(initializationVector + cipher->encryptString(data));
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
    }
}

std::string CipherService::decrypt(const std::string& data, const std::string& passphrase) {
    try {
        std::string decodedData = decode(data);
        auto delimiter = decodedData.begin() + INITIALIZATION_VECTOR_LENGTH;
        std::string initializationVector(decodedData.begin(), delimiter);
        CipherKey key(AES_MODE, passphrase, initializationVector);
        Cipher::Ptr cipher = CipherFactory::defaultFactory().createCipher(key);
        std::string encryptedData(delimiter, decodedData.end());
        return cipher->decryptString(encryptedData);
    } catch (const Exception& exception) {
        Application::instance().logger().error(exception.displayText());
    }
}

std::string CipherService::encode(const std::string& data) {
    std::stringstream encodedStream;
    Base64Encoder encoder(encodedStream);
    encoder.write(reinterpret_cast<const char*>(data.data()), static_cast<int>(data.size()));
    encoder.close();
    return encodedStream.str();
}

std::string CipherService::decode(const std::string& data) {
    std::stringstream encodedStream(data);
    Base64Decoder decoder(encodedStream);
    std::vector<unsigned char> decodedData;

    int character = decoder.get();
    while (character != -1) {
        decodedData.push_back(static_cast<unsigned char>(character));
        character = decoder.get();
    }

    return {decodedData.begin(), decodedData.end()};
}