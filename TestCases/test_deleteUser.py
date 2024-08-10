import pytest
from Utils.customLogger import LogGen
from API_Client_files.Users import APIClient

@pytest.fixture(scope='module')
def api_client():
    return APIClient()

class TestDeleteUser:
    logger=LogGen.loggen()
    def test_updateUser(self, api_client):

        id=7323853
        endpoint=f'users/{id}'
        print ("endpoint is", endpoint)

        
        response=api_client.delete(endpoint)
        print("response received from api is", response)
        print("response code is ", response['status_code'])


        if response is None:
            self.logger.info("Failed to receive response from api")
            pytest.fail("Test Case Failed since no response received from api")
        try:
            print("response code is ", response['status_code'])
            assert response['status_code'] == 204 
            self.logger.info("Test Case Passed")

        except AssertionError as e:
            self.logger.info(f"Test Case Failed since : {e}")
            pytest.fail(f"Test Case Failed: {e}")

        except Exception as e :
            self.logger.info(f"Test Case Failed : {e}")
            pytest.fail(f"Test Case Failed: {e}")




