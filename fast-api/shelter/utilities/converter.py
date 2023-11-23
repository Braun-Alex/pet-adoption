from models.shelter_db_model import ShelterDB
from models.shelter_local_model import ShelterLocalOutput


def convert_from_shelter_db_to_local(shelter_db: ShelterDB) -> ShelterLocalOutput:
    return ShelterLocalOutput(
                                id=shelter_db.id if shelter_db.id is not None else -1,
                                full_name=shelter_db.name if shelter_db.name is not None else "",
                                email=shelter_db.email if shelter_db.email is not None else "",
                                phone_number=shelter_db.number if shelter_db.number is not None else "",
                                description=shelter_db.description if shelter_db.description is not None else "",
                                address=shelter_db.address if shelter_db.address is not None else ""
                            )

