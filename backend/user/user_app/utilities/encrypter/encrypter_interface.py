from abc import ABC, abstractmethod



class Encrypter(ABC):

    @abstractmethod
    def encrypt_data(self, data) -> str | None:
        pass

    @abstractmethod
    def deterministic_encrypt_data(self, data) -> str | None:
        pass

    @abstractmethod
    def decrypt_data(self, encrypted_data) -> str | None:
        pass


