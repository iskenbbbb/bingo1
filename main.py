import asyncio
from dotenv import load_dotenv
from os import getenv
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()
token = getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}")



@dp.message(Command("picture"))
async def send_photo(message: types.Message):
    file = types.FSInputFile("pictures/mem.jpeg")
    await message.answer_photo(file)


@dp.message(Command("info"))
async def info(message: types.Message):
    print(message.from_user)
    await message.answer(
        f"вас завут: {message.from_user.first_name}, "
        f"ваша фамилия: {message.from_user.last_name}, "
        f"ваш id: {message.from_user.id}",
    )



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())