from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher


load_dotenv()
TOKEN = getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
