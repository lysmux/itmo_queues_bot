from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router(name="main")


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    await message.answer("hello")
