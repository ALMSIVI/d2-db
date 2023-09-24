from typing import Any

from sqlalchemy.orm import Session

from d2_db.dto import BodyLocDTO
from d2_db.mediation import BodyLoc
from .__base__ import BaseService


class BodyLocService(BaseService[BodyLocDTO, BodyLoc]):
    __txt__ = 'bodylocs.txt'

    def dto_from_txt(self, row: dict[str, Any], index: int) -> BodyLocDTO | None:
        if row['Body Location'] == 'None':
            return None

        return BodyLocDTO(body_location=row['Body Location'], code=row['Code'])

    def dto_to_mediated(self, dto: BodyLocDTO) -> BodyLoc:
        return BodyLoc(body_location=dto.body_location, code=dto.code)

    def create_table(self):
        BodyLocDTO.metadata.create_all(self.engine)

    def find_by_code(self, code: str) -> BodyLoc | None:
        with Session(self.engine) as session:
            dto = session.get(BodyLocDTO, code)

        return None if dto is None else self.dto_to_mediated(dto)
