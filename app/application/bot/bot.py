import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import BaseStorage
from aiogram_dialog import setup_dialogs
from dishka import AsyncContainer
from dishka.integrations.aiogram import setup_dishka

from app.application.bot.logic import routers
from app.application.bot.runners import run_with_pooling, run_with_webhook
from app.core.settings import Settings

logger = logging.getLogger(__name__)


def create_bot(token: str) -> Bot:
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    return bot


def create_dispatcher(storage: BaseStorage) -> Dispatcher:
    dp = Dispatcher(storage=storage)
    dp.include_routers(*routers)
    setup_dialogs(dp)

    return dp


async def _run_bot(container: AsyncContainer) -> None:
    settings = await container.get(Settings)
    bot = await container.get(Bot)
    dispatcher = await container.get(Dispatcher)

    setup_dishka(container=container, router=dispatcher, auto_inject=True)

    if settings.webhook is None:
        await run_with_pooling(dispatcher=dispatcher, bot=bot)
    else:
        await run_with_webhook(
            bot=bot, dispatcher=dispatcher, settings=settings.webhook
        )


def run_bot(container: AsyncContainer) -> None:
    logger.info("Bot started")

    try:
        asyncio.run(_run_bot(container))
    except (SystemExit, KeyboardInterrupt):
        logger.info("Bot stopped")
