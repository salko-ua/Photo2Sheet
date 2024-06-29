from aiogram import Router, types
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start(message: types.Message) -> None:
    await message.delete()
    text = (
        "Цей бот призначений тільки для використання в групах\n"
        "Володимирської Птахофабрики, не пишіть йому особисто."
    )
    await message.answer(text=text)
