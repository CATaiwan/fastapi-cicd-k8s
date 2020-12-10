import os
from dotenv import load_dotenv

load_dotenv(".env")

DB_HOST = os.getenv("DB_HOST", "")
DB_DATABASE = os.getenv("DB_DATABASE", "")
DB_USERNAME = os.getenv("DB_USERNAME", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
