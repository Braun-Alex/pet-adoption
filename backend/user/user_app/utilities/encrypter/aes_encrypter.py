import hashlib
import base64
import os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from user_app.utilities.encrypter.encrypter_interface import Encrypter

import logging

logger = logging.getLogger(__name__)

class AESEncrypter(Encrypter):
    SECRET_KEY_LENGTH = 32

    def __init__(self) -> None:
        self._secret_key = os.environ['AES_SECRET_KEY']

    @staticmethod
    def hash_data_bytes(data) -> bytes | None:
        if data is None:
            return None
        else:
            sha256 = hashlib.sha256()
            sha256.update(data.encode('utf-8'))
            return sha256.digest()

    def encrypt_data(self, data) -> str | None:
        if data is None:
            return None
        else:
            key = self._secret_key.encode('utf-8')[:self.SECRET_KEY_LENGTH].ljust(self.SECRET_KEY_LENGTH, b'\0')
            initialization_vector = get_random_bytes(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, initialization_vector)
            encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
            return base64.b64encode(initialization_vector + encrypted_data).decode('utf-8')

    def deterministic_encrypt_data(self, data) -> str | None:
        if data is None:
            return None
        else:
            key = self._secret_key.encode('utf-8')[:self.SECRET_KEY_LENGTH].ljust(self.SECRET_KEY_LENGTH, b'\0')
            initialization_vector = self.hash_data_bytes(data)[:AES.block_size]
            cipher = AES.new(key, AES.MODE_CBC, initialization_vector)
            encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
            return base64.b64encode(initialization_vector + encrypted_data).decode('utf-8')

    def decrypt_data(self, encrypted_data) -> str | None:
        if encrypted_data is None:
            return None
        else:
            key = self._secret_key.encode('utf-8')[:self.SECRET_KEY_LENGTH].ljust(self.SECRET_KEY_LENGTH, b'\0')
            encrypted_data = base64.b64decode(encrypted_data)
            initialization_vector = encrypted_data[:AES.block_size]
            encrypted_data = encrypted_data[AES.block_size:]
            cipher = AES.new(key, AES.MODE_CBC, initialization_vector)
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size).decode('utf-8')
            return decrypted_data
    