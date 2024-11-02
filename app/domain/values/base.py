from abc import ABC, abstractmethod
from base64 import b64encode
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject[T](ABC):
    value: T

    @abstractmethod
    def validate(self) -> None:
        pass

    def __post_init__(self) -> None:
        self.validate()


@dataclass(frozen=True)
class Image(BaseValueObject[str]):
    def validate(self) -> None:
        return

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> "Image":
        encoded = b64encode(bytes_)
        return Image(encoded.decode())
