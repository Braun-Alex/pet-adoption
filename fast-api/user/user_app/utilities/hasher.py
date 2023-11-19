from abc import ABC, abstractmethod
import hashlib
import logging

logger = logging.getLogger(__name__)


class HasherInterface(ABC):

    @abstractmethod
    def hash_data(self, data, salt) -> str | None:
        pass


class Hasher(HasherInterface):
    @staticmethod
    def hash_data(data: str, salt: str = None) -> str | None:
        if data is None:
                return None
        else:
            d = data + salt
            sha256 = hashlib.sha256()
            sha256.update(d.encode('utf-8'))
            return sha256.hexdigest()
        
class DummyHasher(HasherInterface):
    @staticmethod
    def hash_data(data: str, salt: str = None) -> str | None:
        logger.info(f"{__class__.__name__} was called. So we won't hash data")
        return data