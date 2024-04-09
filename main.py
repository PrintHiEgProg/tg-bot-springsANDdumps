import logging
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv


from handlers.users import user_router


async def main() -> None:
    load_dotenv('.env')
    if os.getenv("DEBUG"):
        logging.basicConfig(level=logging.INFO)
    token = os.getenv("API_TOKEN")
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())




# Запуск основной функции асинхронно
if __name__ == '__main__':
    asyncio.run(main=main())