from typing import Optional
from sqlalchemy.orm import Session
from animal_app.models.animal_local_model import AnimalLocalIn, AnimalLocalUpdate
from animal_app.models.animal_db_model import AnimalDB


class AnimalController:
    def __init__(self, db: Session) -> None:
        self._db = db

    def create_animal(self, animal: AnimalLocalIn) -> Optional[AnimalDB]:
        animal_db = AnimalDB(**animal.dict())
        self._db.add(animal_db)
        self._db.commit()
        self._db.refresh(animal_db)
        return animal_db
    
    def update_animal(self, animal_id: int, updated_data: AnimalLocalUpdate) -> Optional[AnimalDB]:
        animal_db = self._db.query(AnimalDB).filter(AnimalDB.id == animal_id).first()
        if animal_db:
            for field, value in updated_data.dict().items():
                if value is not None:
                    setattr(animal_db, field, value)
            if updated_data.photo:
                setattr(animal_db, 'photo', updated_data.photo)
                self._db.commit()
                self._db.refresh(animal_db)
                return animal_db
            return None



    def get_animal(self, animal_id: int) -> Optional[AnimalDB]:
        return self._db.query(AnimalDB).filter(AnimalDB.id == animal_id).first()

    def get_all_animals(self) -> list[AnimalDB]:
        return self._db.query(AnimalDB).all()

    def delete_animal(self, animal_id: int) -> bool:
        animal_db = self._db.query(AnimalDB).filter(AnimalDB.id == animal_id).first()
        if animal_db:
            self._db.delete(animal_db)
            self._db.commit()
            return True
        return False
