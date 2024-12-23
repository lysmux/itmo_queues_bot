from collections.abc import AsyncIterator

from dishka import Provider, Scope, from_context, provide
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.settings import Settings


class DefaultProvider(Provider):
    settings = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_redis(self, settings: Settings) -> Redis:
        return Redis(
            host=settings.redis.host,
            port=settings.redis.port,
            password=settings.redis.password,
            db=settings.redis.db,
        )

    @provide(scope=Scope.APP)
    def get_session_maker(self, settings: Settings) -> async_sessionmaker:
        engine = create_async_engine(settings.database.url, pool_pre_ping=True)
        session_maker = async_sessionmaker(bind=engine)

        return session_maker

    @provide(scope=Scope.REQUEST)
    async def get_database_session(
        self, session_maker: async_sessionmaker
    ) -> AsyncIterator[AsyncSession]:
        async with session_maker() as session:
            async with session.begin():
                yield session
