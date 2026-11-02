# config file to pull from env
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")  # db url from .env

ADMIN_KEY = os.getenv("ADMIN_KEY")