from aiogram import Bot, Dispatcher


async def run_with_pooling(bot: Bot, dispatcher: Dispatcher) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)
