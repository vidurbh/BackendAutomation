import pytest
from Utils.customLogger import LogGen
from API_Client_files.Users import APIClient

@pytest.fixture(scope='module')
def api_client():
    return APIClient()

class TestUpdateUser:
    logger=LogGen.loggen()
    body = {
        "name": "testingapinewendpoint",
        "email": "vidubh99@test.com",
        "gender": "female",
        "status": "inactive"
        }

    def test_updateUser(self, api_client):

        id=6940587
        endpoint=f'users/{id}'
        print ("endpoint is", endpoint)

        
        response=api_client.put(endpoint, self.body)
        print("response received from api is", response)

        if response is None:
            self.logger.info("Failed to receive response from api")
            pytest.fail("Test Case Failed since no response received from api")
        try:
            data=response.json()
            print("Data received from responses is " , data)
            assert isinstance(data, dict)
            assert data.get("name") == self.body["name"]
            assert data.get("email") == self.body["email"]
            assert data.get("gender") == self.body["gender"]
            assert data.get("status") == self.body["status"]
            self.logger.info("Test Case Passed")

        except AssertionError as e:
            self.logger.info(f"Test Case Failed : {e}")
            pytest.fail(f"Test Case Failed: {e}")

        except Exception as e :
            self.logger.info(f"Test Case Failed : {e}")
            pytest.fail(f"Test Case Failed: {e}")




