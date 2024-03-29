from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session

from fastapi import HTTPException, status

#from  import Application  # Подразумевается, что модель Application уже определена в вашем приложении
from application_app.models.application_local_models import ApplicationIn, ApplicationOut, ApplicationUpdate
from application_app.models.application_db_models import ApplicationDB

import logging

logger = logging.getLogger(__name__)

class ApplicationControllerInterface(ABC):

    @abstractmethod
    def create_application(self, application_in: ApplicationIn) -> bool:
        """
        Create a new application and return information about it.

        Args:
            application_in (ApplicationIn): The data for creating a new application.

        Returns:
            ApplicationOut: Information about the created application.
        """

    @abstractmethod
    def get_application(self, application_id: int) -> Optional[ApplicationOut]:
        """
        Get information about an application by its ID.

        Args:
            application_id (int): The ID of the application to retrieve.

        Returns:
            Optional[ApplicationOut]: Information about the application if found, else None.
        """

    @abstractmethod
    def get_application_by_shelter_id(self, shelter_id: int) -> Optional[List[ApplicationOut]]:
        """
        Get information about an application by shelter ID.

        Args:
            application_id (int): The ID of the application to retrieve.

        Returns:
            Optional[ApplicationOut]: Information about the application if found, else None.
        """
    
    @abstractmethod
    def get_application_by_user_id(self, user_id: int) -> Optional[List[ApplicationOut]]:
        """
        Get information about an application by shelter ID.

        Args:
            application_id (int): The ID of the application to retrieve.

        Returns:
            Optional[ApplicationOut]: Information about the application if found, else None.
        """

    @abstractmethod
    def update_application(self, application_update: ApplicationUpdate) -> Optional[ApplicationOut]:
        """
        Update information about an application and return the updated information.

        Args:
            application_update (ApplicationUpdate): The data to update the application.

        Returns:
            Optional[ApplicationOut]: Information about the updated application if found, else None.
        """

    @abstractmethod
    def delete_application(self, application_id: int) -> Optional[ApplicationOut]:
        """
        Delete an application by its ID and return information about it if deletion is successful.

        Args:
            application_id (int): The ID of the application to delete.

        Returns:
            Optional[ApplicationOut]: Information about the deleted application if deletion is successful, else None.
        """

    @abstractmethod
    def list_applications(self) -> List[ApplicationOut]:
        """
        Get a list of all applications.

        Returns:
            List[ApplicationOut]: A list of information about all applications.
        """


class ApplicationController(ApplicationControllerInterface):

    def __init__(self, db: Session):
        self._db = db  # You need to inject a database session into the controller

    def __get_application(self, id: int) -> Optional[ApplicationOut]:
        return self._db.query(ApplicationDB).filter(ApplicationDB.id == id).first()
        

    def create_application(self, application_in: ApplicationIn) -> bool:
        new_application = ApplicationDB(**application_in.model_dump())
        self._db.add(new_application)
        self._db.commit()
        self._db.refresh(new_application)
        return True

    def get_application(self, application_id: int) -> Optional[ApplicationOut]:
        application = self.__get_application(id=application_id)
        if application:
            return ApplicationOut(**application.__dict__)
        return None

    def get_application_by_shelter_id(self, shelter_id: int) -> Optional[List[ApplicationOut]]:
        applications = self._db.query(ApplicationDB).filter(ApplicationDB.shelter_id == shelter_id).all()
        logger.info(f"Application Controller: {applications=}")
        if applications:
            applications_local = [ 
                                    ApplicationOut(**application.__dict__)
                                    for application in applications
                                 ]
            
            return applications_local
        applications_local = [ApplicationOut(id=None, user_id=None, animal_id=None, status=None, shelter_id=None)]
        return applications_local
    
    def get_application_by_user_id(self, user_id: int) -> Optional[List[ApplicationOut]]:
        applications = self._db.query(ApplicationDB).filter(ApplicationDB.user_id == user_id).all()
        logger.info(f"Application Controller: {applications=}")
        if applications:
            applications_local = [ 
                                    ApplicationOut(**application.__dict__)
                                    for application in applications
                                 ]
            
            return applications_local
        applications_local = [ApplicationOut(id=None, user_id=None, animal_id=None, status=None, shelter_id=None)]
        return applications_local

    def update_application(self, application_update: ApplicationUpdate) -> Optional[ApplicationOut]:
        logger.info(f"Changing application with id: {application_update.id}")
        application_db = self.__get_application(id=application_update.id)
        if application_db:
            for field, value in application_update.model_dump(exclude={"id"}).items():
                # logger.info(f"{}")
                logger.info(f"Changing {field} --> {value} ")
                setattr(application_db, field, value)
            updated_application_local = ApplicationOut(**application_db.__dict__)
            # application_db.status = application_update.status
            self._db.commit()
            # self._db.refresh(application_db)
            logger.info(f"Updated object: {updated_application_local=}")
            return updated_application_local
        return None

    def delete_application(self, application_id: int) -> Optional[ApplicationOut]:
        application = self.get_application(application_id)
        if application:
            self._db.delete(application)
            self._db.commit()
            return ApplicationOut(**application.__dict__)
        return None

    def list_applications(self) -> List[ApplicationOut]:
        applications = self._db.query(ApplicationDB).all()
        return [ApplicationOut(**application.__dict__) for application in applications]
