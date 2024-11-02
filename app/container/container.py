from dishka import AsyncContainer, make_async_container

from app.container.providers import (
    BotProvider,
    DefaultProvider,
    InfrastructureProvider,
    LogicProvider,
)
from app.core.settings import Settings


def init_container(settings: Settings) -> AsyncContainer:
    return make_async_container(
        DefaultProvider(),
        InfrastructureProvider(),
        LogicProvider(),
        BotProvider(),
        context={Settings: settings},
    )
