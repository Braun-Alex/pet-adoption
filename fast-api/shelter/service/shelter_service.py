from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal
from utilities.utilities import hash_data
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from utilities.utilities import TokenSchema, create_access_token, create_refresh_token


class ShelterServiceInterface:
    def register_shelter(self, success: bool):
        pass

    def authorize_shelter(self, tokens: TokenSchema):
        pass


class ShelterService(ShelterServiceInterface):
    def __init__(self, shelter_controller: ShelterController):
        self._shelter_controller = shelter_controller

    def register_shelter(self, shelter: ShelterLocal) -> bool:
        shelter_db = self._shelter_controller.get_shelter_by_email(shelter.email)

        if shelter_db:
            raise HTTPException(status.HTTP_409_CONFLICT)

        return self._shelter_controller.create_shelter(shelter)

    def authorize_shelter(self, shelter: OAuth2PasswordRequestForm) -> TokenSchema:
        shelter_db = self._shelter_controller.get_shelter_by_email(shelter.username)
        print(f"{shelter_db=}")
        if not shelter_db or hash_data(shelter.password + shelter_db.salt) != shelter_db.password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        return {
            "access_token": create_access_token(shelter_db),
            "refresh_token": create_refresh_token(shelter_db),
        }
