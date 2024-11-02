from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class BaseEntity(ABC):  # noqa: B024
    pass


@dataclass
class IDMixin:
    id: str = field(default_factory=lambda: str(uuid4()), kw_only=True)

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IDMixin):
            return False
        return self.id == other.id


@dataclass
class CreatedAtMixin:
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)


@dataclass
class IsDeletedMixin:
    is_deleted: bool = field(default=False, kw_only=True)
