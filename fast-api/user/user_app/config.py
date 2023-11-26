import logging
import json

from user_app.service.user_service import UserServiceInterface
from user_app.database import Base, engine, SessionLocal

from sqlalchemy.orm import sessionmaker
from user_app.service.user_service import UserService

from user_app.controllers.user_controller import UserController

from user_app.utilities.encrypter.dummy_encrypter import DummyEncrypter
from user_app.utilities.encrypter.aes_encrypter import AESEncrypter

from user_app.utilities.hasher import Hasher, DummyHasher

from sqlalchemy.exc import OperationalError

CONFIG_FILE = "/app/user_app/user_app_config.json"

logger = logging.getLogger(__name__)

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.info("Config file not found.")
        return {}


def config_service() -> UserServiceInterface:
    config = load_config()
   

    try:
    # Попытка установления соединения   
        Base.metadata.create_all(bind=engine)
       
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        # Если успешно установлено соединение
        logger.info("Connection established successfully")

        # Здесь вы можете выполнять операции с базой данных

        # Не забудьте закрыть соединение, когда оно больше не нужно
    except Exception as e:
    # Обработка ошибки установления соединения
        logger.error(f"Connection error: {e}")


    logger.info(f"{config=}")

    is_encrypt_data = config.get("encrypt_data", False)
    logger.info(f"{is_encrypt_data=}")

    is_hash_data = config.get("hash_data", False)

    if is_encrypt_data:
        logger.info("Data encryption is turned ON")
        encrypter=AESEncrypter()
    else:
        logger.info("Data encryption is turned OFF")
        encrypter=DummyEncrypter()

    if is_hash_data:
        logger.info("Data hashing is turned ON")
        hasher = Hasher()
    else:
        logger.info("Data hashing is turned OFF")
        hasher = DummyHasher
    
    user_controller = UserController(db=db, encrypter=encrypter, hasher=hasher)
    
    return UserService(user_controller=user_controller) 



