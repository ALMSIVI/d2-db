from sqlalchemy.orm import Mapped, mapped_column

from .__base__ import BaseDTO


class PlayerClassDTO(BaseDTO):
    __tablename__ = 'playerclass'

    id: Mapped[int] = mapped_column(primary_key=True)
    player_class: Mapped[str]
    code: Mapped[str]
