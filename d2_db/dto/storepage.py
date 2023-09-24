from sqlalchemy.orm import Mapped, mapped_column

from .__base__ import BaseDTO


class StorePageDTO(BaseDTO):
    __tablename__ = 'storepage'

    store_page: Mapped[str]
    code: Mapped[str] = mapped_column(primary_key=True)
