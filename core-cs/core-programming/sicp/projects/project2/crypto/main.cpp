#include <cryptlib.h>
#include <modes.h>
#include <aes.h>
#include <filters.h>
#include <hex.h>

using namespace CryptoPP;

std::string encryptMessage(const std::string &message, const std::string &key)
{
    ECB_Mode<AES>::Encryption ecbEncryption((byte *)key.data(), AES::DEFAULT_KEYLENGTH);

    std::string cipher;
    StringSource(message, true, new StreamTransformationFilter(ecbEncryption, new StringSink(cipher)));
    return cipher;
}

std::string decryptMessage(const std::string &cipher, const std::string &key)
{
    ECB_Mode<AES>::Decryption ecbDecryption((byte *)key.data(), AES::DEFAULT_KEYLENGTH);

    std::string decryptedMessage;
    StringSource(cipher, true, new StreamTransformationFilter(ecbDecryption, new StringSink(decryptedMessage)));
    return decryptedMessage;
}
