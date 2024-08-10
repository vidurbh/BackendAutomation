import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://gorest.co.in/public/v2")
    
    API_KEY = os.getenv("API_KEY", "60d072f307c76009106b5174d6f4567e0521567e668fa89d420a715c82b81d58")
    
    HEADERS = {
        "Authorization": "Bearer " + "60d072f307c76009106b5174d6f4567e0521567e668fa89d420a715c82b81d58",
        "Content-Type": "application/json"
    }
    
    TIMEOUT = int(os.getenv("TIMEOUT", 30))
    
