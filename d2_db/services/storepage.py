from typing import Any

from sqlalchemy.orm import Session

from d2_db.dto import StorePageDTO
from d2_db.mediation import StorePage
from .__base__ import BaseService


class StorePageService(BaseService[StorePageDTO, StorePage]):
    __txt__ = 'storepage.txt'

    def dto_from_txt(self, row: dict[str, Any], index: int) -> StorePageDTO:
        return StorePageDTO(store_page=row['Store Page'], code=row['Code'])

    def dto_to_mediated(self, dto: StorePageDTO) -> StorePage:
        return StorePage(store_page=dto.store_page, code=dto.code)

    def create_table(self):
        StorePageDTO.metadata.create_all(self.engine)

    def find_by_code(self, code: str) -> StorePage | None:
        with Session(self.engine) as session:
            dto = session.get(StorePageDTO, code)

        return None if dto is None else self.dto_to_mediated(dto)
