from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from app.domain.entities.base import BaseEntity


@dataclass
class BaseDTO[E: BaseEntity](ABC):
    @classmethod
    @abstractmethod
    def from_entity(cls, entity: E) -> "BaseDTO":
        pass

    @abstractmethod
    def to_entity(self) -> E:
        pass


@dataclass
class IDMixin:
    id: str


@dataclass
class CreatedAtMixin:
    created_at: datetime


@dataclass
class IsDeletedMixin:
    is_deleted: bool
