from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Query(ABC):  # noqa: B024
    pass


@dataclass(eq=False, frozen=True)
class QueryHandler[T](ABC):
    @abstractmethod
    async def handle(self, query: Query) -> T:
        pass
