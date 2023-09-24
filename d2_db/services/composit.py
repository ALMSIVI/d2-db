from typing import Any

from sqlalchemy.orm import Session

from d2_db.dto import CompositeDTO
from d2_db.mediation import Composit
from .__base__ import BaseService


class CompositService(BaseService[CompositeDTO, Composit]):
    __txt__ = 'composit.txt'

    def dto_from_txt(self, row: dict[str, Any], index: int) -> CompositeDTO | None:
        return CompositeDTO(id=index, name=row['Name'], token=row['Token'])

    def dto_to_mediated(self, dto: CompositeDTO) -> Composit:
        return Composit(id=dto.id, name=dto.name, token=dto.token)

    def create_table(self):
        CompositeDTO.metadata.create_all(self.engine)

    def find_by_id(self, player_class_id: str) -> Composit | None:
        with Session(self.engine) as session:
            dto = session.get(CompositeDTO, player_class_id)

        return None if dto is None else self.dto_to_mediated(dto)
