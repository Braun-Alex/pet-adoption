from user_app.utilities.encrypter.encrypter_interface import Encrypter

import logging

logger = logging.getLogger(__name__)

class DummyEncrypter(Encrypter):

    def encrypt_data(self, data) -> str | None:
        logger.info(f"{__class__.__name__} was called. So we won't ecrypt data")
        return data

    def deterministic_encrypt_data(self, data) -> str | None:
        logger.info(f"{__class__.__name__} was called. So we won't ecrypt data")

        return data

    def decrypt_data(self, encrypted_data) -> str | None:
        logger.info(f"{__class__.__name__} was called. So we won't decrypt data")
        return encrypted_data
