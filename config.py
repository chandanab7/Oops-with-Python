from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    # Add other configuration variables as needed, e.g., database URI, API keys, etc.   
    