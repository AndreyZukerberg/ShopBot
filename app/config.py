from os import getenv
from dotenv import load_dotenv

load_dotenv()

Bot_Token = getenv("TOKEN")

if not Bot_Token:
    raise ValueError("TOKEN не найден в .env")