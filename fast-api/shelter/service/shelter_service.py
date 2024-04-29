from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal, ShelterLocalRegistration, ShelterLocalUpdate
from utilities.utilities import hash_data
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from utilities.utilities import TokenSchema, create_access_token, create_refresh_token
import httpx
import os
import logging

logger = logging.getLogger(__name__)


class ShelterServiceInterface:
    def register_shelter(self, success: bool):
        pass

    def authorize_shelter(self, tokens: TokenSchema):
        pass

    def get_shelter(self, shelter: str):
        pass

    def update_shelter_info(self, new_shelter_info: ShelterLocalUpdate) -> bool:
        pass

    def remove_shelter(self, shelter_id: int) -> bool:
        pass


class ShelterService(ShelterServiceInterface):
    def __init__(self, shelter_controller: ShelterController):
        self._shelter_controller = shelter_controller

    def register_shelter(self, shelter: ShelterLocalRegistration) -> bool:
        shelter_local = self._shelter_controller.get_shelter_by_email(shelter.email)

        if shelter_local:
            raise HTTPException(status.HTTP_409_CONFLICT)

        return self._shelter_controller.create_shelter(shelter)

    def authorize_shelter(self, shelter: OAuth2PasswordRequestForm) -> TokenSchema:
        shelter_db = self._shelter_controller._get_shelter_by_email(shelter.username)
        if not shelter_db or hash_data(shelter.password + shelter_db.salt) != shelter_db.password:
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
    
    def remove_shelter(self, token:str, shelter_id: int) -> bool:
        self.delete_all_animals(token=token)
        return self._shelter_controller.remove_shelter(shelter_id=shelter_id)

    def delete_all_animals(self, token: str)->bool:
        # request = f"{os.getenv('ANIMAL_SERVICE_HOST_URL')}delete_all_by_shelter"
        # request = f"http://animal_service:8000/api/v1/animals/delete_all_by_shelter"
        request = f"http://animal_service:8000/api/v1/animals/delete_all_by_shelter"
        headers = {"Authorization": f"Bearer {token}"}
        logger.info(f"Sending DELETE request to {request=}")
        return httpx.delete(request, headers=headers)


        

        