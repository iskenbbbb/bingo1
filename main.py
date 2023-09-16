import asyncio
import logging
from bot import bot, dp
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.film import film_router



async def main():
    dp.include_router(start_router)
    dp.include_router(film_router)

    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
