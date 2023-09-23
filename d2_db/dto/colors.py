from sqlalchemy.orm import Mapped, mapped_column

from .__base__ import BaseDTO


class ColorDTO(BaseDTO):
    __tablename__ = 'colors'

    id: Mapped[int] = mapped_column(primary_key=True)
    transform_color: Mapped[str]
    code: Mapped[str]
