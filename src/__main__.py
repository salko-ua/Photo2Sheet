import aiogram
import apykuma
import asyncio
import logging

from src.config import BOT_TOKEN, KUMA_TOKEN
from src.handlers import main


async def register_handlers(dp: aiogram.Dispatcher) -> None:
    dp.include_router(main.router)


async def start_bot() -> None:
    if KUMA_TOKEN != "":
        await apykuma.start(url=KUMA_TOKEN, delay=15)

    bot = aiogram.Bot(token=BOT_TOKEN)
    dispatcher = aiogram.Dispatcher()

    await register_handlers(dispatcher)
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_bot())