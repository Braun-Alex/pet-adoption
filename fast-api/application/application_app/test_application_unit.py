from application_app.service.application_service import ApplicationService
from application_app.controllers.application_controller import ApplicationController
from application_app.models.application_local_models import  ApplicationOut, ApplicationStatus
from application_app.application import get_application
import yaml
import logging.config

from fastapi import status, HTTPException

import pytest
from unittest.mock import patch

with open('/app/logger_conf.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

class ApplicationServiceData:
    def __init__(self, get_application_by_shelter_id_ret_val: ApplicationOut = None, get_application_by_user_id_ret_val: ApplicationOut = None):
        self.get_application_by_shelter_id_ret_val = get_application_by_shelter_id_ret_val
        self.get_application_by_user_id_ret_val = get_application_by_user_id_ret_val
        

def setup_application_service_mock(mock_application_service, application_data: ApplicationServiceData):
    mock_application_service.get_application_by_shelter_id.return_value = application_data.get_application_by_shelter_id_ret_val   
    mock_application_service.get_application_by_user_id.return_value    = application_data.get_application_by_user_id_ret_val

application_by_sh = ApplicationOut(id=1, shelter_id=1, user_id=1, status=ApplicationStatus.CREATED)
application_by_user = ApplicationOut(id=2, shelter_id=1, user_id=2, status=ApplicationStatus.CREATED)

@pytest.mark.parametrize( "application_service_data, shelter_id, user_id, expected_result", 
                            [ 
                                pytest.param(ApplicationServiceData(get_application_by_shelter_id_ret_val=application_by_sh, get_application_by_user_id_ret_val=application_by_user), 1, None, application_by_sh,  id="Get application by shelter_id"),
                                pytest.param(ApplicationServiceData(get_application_by_shelter_id_ret_val=application_by_sh, get_application_by_user_id_ret_val=application_by_user), None, 2, application_by_user, id="Get application by user_id"),
                                pytest.param(ApplicationServiceData(get_application_by_shelter_id_ret_val=application_by_sh, get_application_by_user_id_ret_val=application_by_user), None, None, status.HTTP_400_BAD_REQUEST, id="Both parameters are None"),
                                pytest.param(ApplicationServiceData(get_application_by_shelter_id_ret_val=application_by_sh, get_application_by_user_id_ret_val=application_by_user), 2, 1, status.HTTP_400_BAD_REQUEST, id="Both parameters are not None"),
                            ],
                        )
@patch("application_app.application.application_service")
def test_get_appl(mock_application_service, application_service_data, user_id, shelter_id, expected_result):
    setup_application_service_mock(mock_application_service, application_service_data)
    logger.info(f"get_application_by_user_id: {mock_application_service.get_application_by_user_id()}")
    logger.info(f"{user_id=}, {shelter_id=}, {expected_result=}")
    try:
        result = get_application(shelter_id=shelter_id, user_id=user_id)
        assert result == expected_result, f"Expected {expected_result}, but got {result}"
    except HTTPException as e:
        assert e.status_code == expected_result, f"Expected {expected_result}, but got {e.status_code}"