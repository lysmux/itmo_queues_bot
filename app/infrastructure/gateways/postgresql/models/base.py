from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID, DateTime, MetaData, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)


class BaseORM(DeclarativeBase):
    metadata = metadata
    __allow_unmapped__ = False


class IDMixin:
    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, unique=True, default=lambda: str(uuid4())
    )


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class IsDeletedMixin:
    is_deleted: Mapped[bool] = mapped_column(default=False)
