import requests
from Utils.customLogger import LogGen
import pytest
from API_Client_files.Users import APIClient

@pytest.fixture(scope="module")
def api_client():
        return APIClient()


class Testusers:
    logger=LogGen.loggen()
    
    def test_getUser(self,api_client):
        response=api_client.get('users')
        print('response of api: ', response)

        try:
            assert response is not None
            assert isinstance(response, list)
            assert len(response)>0
            self.logger.info("Test Case passed")
        except AssertionError as e:
            self.logger.error(f"An error occurred: {e}")
        except Exception as e:
            self.logger.error("An error occurred: ", e)

            





