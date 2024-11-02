import asyncio

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from app.core.settings.webhook import WebhookSettings


async def run_with_webhook(
    bot: Bot, dispatcher: Dispatcher, settings: WebhookSettings
) -> None:
    app = web.Application()
    runner = web.AppRunner(app)

    # setup requests handler
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dispatcher, bot=bot, secret_token=settings.secret
    )
    webhook_requests_handler.register(app, path=settings.path)
    setup_application(app, dispatcher)

    # setup aiohttp server
    await runner.setup()
    webhook_site = web.TCPSite(runner, host="0.0.0.0", port=settings.listen_port)

    await bot.set_webhook(url=settings.url, secret_token=settings.secret)

    try:
        await webhook_site.start()
        await asyncio.Event().wait()
    finally:
        await runner.cleanup()
