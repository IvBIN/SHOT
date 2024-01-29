import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import main as mainrun


async def main():
    print("Bot started")
    bot = Bot(TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(
        mainrun.router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot dead")