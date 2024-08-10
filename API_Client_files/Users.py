import requests
from API_Client_files.config import Config

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS
        self.timeout = Config.TIMEOUT

    def get_url(self, endpoint):
        return self.base_url + "/" + endpoint

    def get(self, endpoint, params=None):
        url = self.get_url(endpoint)
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
            return response.json()
        except requests.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(self, endpoint, data=None):
        
        url = self.get_url(endpoint)
        try:
            response = requests.post(url, headers=self.headers, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response 
        except requests.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    def put(self, endpoint, data=None):
        url = self.get_url(endpoint)
        try:
            response = requests.put(url, headers=self.headers, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"PUT request failed: {e}")
            return None

    def delete(self, endpoint):
        url = self.get_url(endpoint)
        try:
            response = requests.delete(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return {
                    'status_code': response.status_code,
                    'response': response.json() if response.status_code != 204 else None
            } 
            
        except requests.RequestException as e:
            print(f"DELETE request failed: {e}")
            return {'status_code': None, 'response': None}
