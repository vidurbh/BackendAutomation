from Utils.customLogger import LogGen
import pytest
from API_Client_files.Users import APIClient

@pytest.fixture(scope="module")
def api_client():
        return APIClient()

class Testusers:
    logger=LogGen.loggen()

    def test_createUser(self,api_client):

        body = {
        "name": "testingapinewendpoint",
        "email": "vidubh290@test.com",
        "gender": "female",
        "status": "active"
        }
        response=api_client.post('users', body)
        print('response of api: ', response)

        if response is None:
            self.logger.info("No response received from API. Test case failed.")
            pytest.fail("No response received from API.")
        try:
                data=response.json()
                print('response data', data)
                assert 'id' in data
                assert data['name']==body["name"]
                assert data["email"] == body["email"]
                assert data["gender"] == body["gender"]
                assert data["status"] == body["status"]
                self.logger.info("Test Case passed for create user")

        except AssertionError as e:
                self.logger.info(f"Test Case failed for create user: {e}")
                raise  

        except Exception as e:
                self.logger.info(f"Test Case failed for create user: {e}")
                raise  


        

              









