from sqlalchemy.orm import Mapped, mapped_column

from .__base__ import BaseDTO


class EventDTO(BaseDTO):
    __tablename__ = 'events'

    event: Mapped[str]
    description: Mapped[str] = mapped_column(primary_key=True)
