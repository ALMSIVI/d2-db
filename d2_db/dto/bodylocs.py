from sqlalchemy.orm import Mapped, mapped_column

from .__base__ import BaseDTO


class BodyLocDTO(BaseDTO):
    __tablename__ = 'bodylocs'

    body_location: Mapped[str]
    code: Mapped[str] = mapped_column(primary_key=True)
