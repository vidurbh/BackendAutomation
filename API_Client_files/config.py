import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    print ("Base URL is", BASE_URL)
    
    API_KEY = os.getenv("API_KEY")
    print ("API Key is", API_KEY)

    
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}" ,
        "Content-Type": "application/json"
    }
    
    TIMEOUT = int(os.getenv("TIMEOUT", 30))
    
