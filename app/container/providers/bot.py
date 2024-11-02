from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.base import BaseStorage, DefaultKeyBuilder, KeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from dishka import Provider, Scope, provide
from redis.asyncio import Redis

from app.application.bot.bot import create_bot, create_dispatcher
from app.core.settings import Settings


class BotProvider(Provider):
    @provide(scope=Scope.APP)
    def dispatcher(self, storage: BaseStorage) -> Dispatcher:
        return create_dispatcher(storage=storage)

    @provide(scope=Scope.APP)
    def bot(self, settings: Settings) -> Bot:
        return create_bot(token=settings.bot.token)

    @provide(scope=Scope.APP)
    def storage(
        self, settings: Settings, redis: Redis, key_builder: KeyBuilder
    ) -> BaseStorage:
        ttl = settings.bot.sessions_ttl
        return RedisStorage(
            redis=redis, data_ttl=ttl, state_ttl=ttl, key_builder=key_builder
        )

    @provide(scope=Scope.APP)
    def key_builder(self) -> KeyBuilder:
        return DefaultKeyBuilder(with_destiny=True)
