from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Command(ABC):  # noqa: B024
    pass


@dataclass(eq=False, frozen=True)
class CommandHandler[T](ABC):
    @abstractmethod
    async def handle(self, command: Command) -> T:
        pass
