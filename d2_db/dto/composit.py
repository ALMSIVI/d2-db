from sqlalchemy.orm import Mapped, mapped_column

from .__base__ import BaseDTO


class CompositeDTO(BaseDTO):
    __tablename__ = 'composit'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    token: Mapped[str]
