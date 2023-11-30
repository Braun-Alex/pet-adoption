from abc import ABC, abstractmethod
from typing import List, Optional

from application_app.models.application_local_models import ApplicationIn, ApplicationOut, ApplicationUpdate
from application_app.controllers.application_controller import ApplicationControllerInterface

from fastapi import status, HTTPException

import logging

logger = logging.getLogger(__name__)

class ApplicationServiceInterface(ABC):

    @abstractmethod
    def add_application(self, application_in: ApplicationIn) -> bool:
        """
        Add a new application and return information about it.

        Args:
            application_in (ApplicationIn): The data for creating a new application.

        Returns:
            bool: bool flag of operation
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
    def get_application_by_shelter_id(self, shleter_id: int) -> Optional[ApplicationOut]:
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
    def user_exists(self, user_id: int) -> bool:
        """
        Check if a user with the given ID exists.

        Args:
            user_id (int): The ID of the user to check.

        Returns:
            bool: True if the user exists, else False.
        """

    @abstractmethod
    def shelter_exists(self, shelter_id: int) -> bool:
        """
        Check if a shelter with the given ID exists.

        Args:
            shelter_id (int): The ID of the shelter to check.

        Returns:
            bool: True if the shelter exists, else False.
        """

class ApplicationService(ApplicationServiceInterface):

    def __init__(self, controller: ApplicationControllerInterface):
        self._controller = controller

    def add_application(self, application_in: ApplicationIn) -> bool:
        if  self.user_exists(user_id=application_in.user_id) == False or \
            self.shelter_exists(shelter_id=application_in.shelter_id)==False:

         raise HTTPException(status.HTTP_400_BAD_REQUEST)

        return self._controller.create_application(application_in)


    def get_application(self, application_id: int) -> Optional[ApplicationOut]:
        return self._controller.get_application(application_id)
    
    def get_application_by_shelter_id(self, shelter_id: int) -> Optional[ApplicationOut]:
        logger.info(f"Application Service: {shelter_id=}")
        return self._controller.get_application_by_shelter_id(shelter_id=shelter_id)

    def update_application(self, application_update: ApplicationUpdate) -> Optional[ApplicationOut]:
<<<<<<< HEAD
        updated_application = self._controller.update_application(application_update)
        logger.info(f"{updated_application=}")
        return updated_application
=======
        return self._controller.update_application(application_update)
>>>>>>> main

    def delete_application(self, application_id: int) -> Optional[ApplicationOut]:
        return self._controller.delete_application(application_id)

    def user_exists(self, user_id: int) -> bool:
       """
            At this moment is a dump method with return True.
            TODO: send request to user_service to verify if user exists
       """
       return True


    def shelter_exists(self, shelter_id: int) -> bool:
       """
            At this moment is a dump method with return True.
            TODO: send request to shelter_service to verify if user exists
       """
       return True


