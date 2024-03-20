from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal, ShelterLocalRegistration, ShelterLocalUpdate
from utilities.utilities import hash_data
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from utilities.utilities import TokenSchema, create_access_token, create_refresh_token


class ShelterServiceInterface:
    def register_shelter(self, success: bool):
        pass

    def authorize_shelter(self, tokens: TokenSchema):
        pass

    def get_shelter(self, shelter: str):
        pass
    def update_shelter_info(self, new_shelter_info: ShelterLocalUpdate) -> bool:
        pass


class ShelterService(ShelterServiceInterface):
    def __init__(self, shelter_controller: ShelterController):
        self._shelter_controller = shelter_controller

    def register_shelter(self, shelter: ShelterLocalRegistration) -> bool:
        shelter_db = self._shelter_controller.get_shelter_by_email(shelter.email)

        if shelter_db:
            raise HTTPException(status.HTTP_409_CONFLICT)

        return self._shelter_controller.create_shelter(shelter)

    def authorize_shelter(self, shelter: OAuth2PasswordRequestForm) -> TokenSchema:
        shelter_db = self._shelter_controller.get_shelter_by_email(shelter.username)
        #if not shelter_db or hash_data(shelter.password + shelter_db.salt) != shelter_db.password:
        if not shelter_db or shelter.password != shelter_db.password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        return {
            "access_token": create_access_token(shelter_db.id),
            "refresh_token": create_refresh_token(shelter_db.id),
        }

    def get_shelter(self, shelter_id: int) -> str:
        shelter_local = self._shelter_controller.get_shelter_by_id(shelter_id)
        if not shelter_local:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return shelter_local


    def update_shelter_info(self, new_shelter_info: ShelterLocalUpdate) -> bool:
        return self._shelter_controller.update_shelter_info(shelter_data=new_shelter_info)

        