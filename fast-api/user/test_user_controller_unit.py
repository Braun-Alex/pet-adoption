import pytest
from unittest.mock import Mock
from user_app.controllers.user_controller import UserController  # Replace 'your_module' with the actual module where UserController is defined
from user_app.utilities.encrypter.aes_encrypter import Encrypter
from user_app.utilities.hasher import HasherInterface
from fastapi import HTTPException  # Replace 'your_exceptions' with the module where HTTPException is defined

from user_app.models.user_local_model import UserLocalRegistration

from sqlalchemy.orm import Session


# Mocked dependencies
@pytest.fixture
def db()->Session:
    return Mock()

@pytest.fixture
def encrypter() -> Encrypter:
    return Mock()

@pytest.fixture
def hasher()->HasherInterface:
    return Mock()

# Create a UserController instance with mocked dependencies
@pytest.fixture
def user_controller(db, encrypter, hasher)-> UserController:
    return UserController(db, encrypter, hasher)

# Test creating a user successfully
def test_create_user_successful(user_controller: UserController, db: Session, encrypter: Encrypter, hasher:HasherInterface):
    user_data = UserLocalRegistration(email="test@example.com", full_name="John Doe", password="password123") 
    
    # Mock the necessary methods
    encrypter.deterministic_encrypt_data.return_value = "encrypted_data"
    hasher.hash_data.return_value = "hashed_password"
    
    result = user_controller.create_user(user_data)

    assert result is True
    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()

# Test getting a user by ID
def test_get_user_by_id(user_controller:UserController, db: Session):
    user_id = 1
    db.query.return_value.filter.return_value.first.return_value = {"id": user_id}
    
    result = user_controller.get_user_by_id(user_id)

    assert result == {"id": user_id}

# Test getting a user by email
def test_get_user_by_email(user_controller:UserController, db:Session, encrypter:Encrypter):
    email = "test@example.com"
    encrypted_email = "encrypted_email"
    db.query.return_value.filter.return_value.first.return_value = {"email": encrypted_email}
    
    # Mock the encrypter
    encrypter.deterministic_encrypt_data.return_value = encrypted_email
    
    result = user_controller.get_user_by_email(email)

    assert result == {"email": encrypted_email}
