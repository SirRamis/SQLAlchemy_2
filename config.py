from dotenv import load_dotenv
import os

load_dotenv()

DB_DRIVER = os.getenv("DB_DRIVER"),
DB_USERNAME = os.getenv("DB_USERNAME"),
DB_PASSWORD = os.getenv("DB_PASSWORD"),
DB_HOST = os.getenv("DB_HOST"),
DB_PORT = os.getenv("DB_PORT"),
DB_NAME = os.getenv("DB_NAME")
DB_NAME2 = os.getenv("DB_NAME2")
