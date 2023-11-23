from shelter.models.shelter_db_model import ShelterDB
from shelter.models.shelter_local_model import ShelterLocalOutput


def convert_from_shelter_db_to_local(shelter_db: ShelterDB):
    return ShelterLocalOutput(
                                id=shelter_db.id, 
                                full_name=shelter_db.name, 
                                email=shelter_db.email, 
                                phone_number=shelter_db.number, 
                                description=shelter_db.description
                            )

