from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from d2_db.dto.__base__ import BaseDTO

T = TypeVar('T', bound=BaseDTO)
S = TypeVar('S', bound=BaseModel)


class BaseService(Generic[T, S], ABC):
    __txt__: str
    engine: Engine

    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def create_table(self):
        raise NotImplementedError

    @abstractmethod
    def dto_from_txt(self, row: dict[str, Any], index: int) -> T:
        return NotImplemented

    @abstractmethod
    def dto_to_mediated(self, dto: T) -> S:
        return NotImplemented

    def save_all(self, dtos: list[T]):
        with Session(self.engine) as session:
            session.add_all(dtos)
            session.commit()
