from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
# from handlers.texts import DRAM_FILMS


film_router = Router()


@film_router.message(Command("film"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Фильмы"),
                KeyboardButton(text="Мультфильмы"),
            ],
            [
                KeyboardButton(text="Серилы"),
            ],
        ],
        resize_keyboard=True,
    )
    await message.answer(f"Выберите категирию ниже:", reply_markup=kb)



# обработчик фильмов


@film_router.message(F.text == "Фильмы")
async def show_film(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="Драма"),
                KeyboardButton(text="Боевик"),
            ],
            [
                KeyboardButton(text="Криминал"),
                KeyboardButton(text="Комедия"),
            ],
            [
                KeyboardButton(text="Фантастика"),
                KeyboardButton(text="Ужасы"),
            ],
        ],
        resize_keyboard = True,
    )
    await message.answer(f"Выберите категирию ниже:", reply_markup=kb)




    # пока заглушка

@film_router.message(F.text == "Драма")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список Драм:", reply_markup=kb)

@film_router.message(F.text == "Боевик")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список боевиков:", reply_markup=kb)


@film_router.message(F.text == "Криминал")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список криминалов:", reply_markup=kb)


@film_router.message(F.text == "Комедия")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список комедий:", reply_markup=kb)



@film_router.message(F.text == "Фантастика")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список фантастика:", reply_markup=kb)


@film_router.message(F.text == "Ужасы")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список ужасов:", reply_markup=kb)



#обработчик мультиков
@film_router.message(F.text == "Мультфильмы")
async def show_film(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="Анимация"),
                KeyboardButton(text="Приключения"),
            ],
            [
                KeyboardButton(text="Мюзикл"),
                KeyboardButton(text="Аниме"),
            ],
            [
                KeyboardButton(text="Фантастика"),
                KeyboardButton(text="Ужасы"),
            ],
        ],
        resize_keyboard = True,
    )
    await message.answer(f"Выберите мультфильм ниже ниже:", reply_markup=kb)



#обработчик мультиков
@film_router.message(F.text == "Анмация")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список анимаций:", reply_markup=kb)


@film_router.message(F.text == "Приключения")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список приключений:", reply_markup=kb)



@film_router.message(F.text == "Мюзикл")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список мюзиклов:", reply_markup=kb)


@film_router.message(F.text == "Аниме")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список аниме:", reply_markup=kb)


@film_router.message(F.text == "Фантастика")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список Драм:", reply_markup=kb)


@film_router.message(F.text == "Ужасы")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список ужасов:", reply_markup=kb)