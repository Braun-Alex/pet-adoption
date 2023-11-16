from typing import Optional
from models.shelter_local_model import ShelterLocal
from controllers.shelter_controller import ShelterController
from fastapi import HTTPException
from utilities.utilities import HTTPResponse, hash_data


class ShelterServiceInterface:
    def register_shelter(self, shelter_local: ShelterLocal):
        pass

    def authorize_shelter(self, shelter_local: ShelterLocal):
        pass


class ShelterService(ShelterServiceInterface):
    def __init__(self, shelter_controller: ShelterController):
        self._shelter_controller = shelter_controller

    def register_shelter(self, shelter: ShelterLocal) -> ShelterLocal:
        shelter_db = self._shelter_controller.get_shelter_by_email(shelter.email)

        if shelter_db:
            raise HTTPException(HTTPResponse.CONFLICT.value)

        shelter_db = self._shelter_controller.create_shelter(shelter)
        print(f"{str(shelter_db)=}")

        return ShelterLocal(id=shelter_db.id, email=shelter_db.email, name=shelter_db.name)

    def authorize_shelter(self, shelter: ShelterLocal) -> Optional[ShelterLocal]:
        shelter_db = self._shelter_controller.get_shelter_by_email(shelter.email)
        print(f"{shelter_db=}")
        if not shelter_db or hash_data(shelter.password + shelter_db.salt) != shelter_db.password:
            raise HTTPException(HTTPResponse.UNAUTHORIZED.value)

        return ShelterLocal(id=shelter_db.id, email=shelter_db.email, name=shelter_db.name)
