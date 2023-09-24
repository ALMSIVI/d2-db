from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from d2_db.dto import PlayerClassDTO
from d2_db.mediation import PlayerClass
from .__base__ import BaseService


class PlayerClassService(BaseService[PlayerClassDTO, PlayerClass]):
    __txt__ = 'playerclass.txt'

    def dto_from_txt(self, row: dict[str, Any], index: int) -> PlayerClassDTO | None:
        # There is an "Expansion" row that doesn't correspond to any characters.
        # We need to exclude that and adjust the index accordingly.
        if row['Player Class'] == 'Expansion':
            return None

        return PlayerClassDTO(id=index, player_class=row['Player Class'], code=row['Code'])

    def dto_to_mediated(self, dto: PlayerClassDTO) -> PlayerClass:
        return PlayerClass(id=dto.id, player_class=dto.player_class, code=dto.code)

    def create_table(self):
        PlayerClassDTO.metadata.create_all(self.engine)

    def find_by_id(self, player_class_id: str) -> PlayerClass | None:
        with Session(self.engine) as session:
            dto = session.get(PlayerClassDTO, player_class_id)

        return None if dto is None else self.dto_to_mediated(dto)

    def find_by_code(self, code: str) -> PlayerClass | None:
        stmt = select(PlayerClassDTO).where(PlayerClassDTO.code == code)
        with Session(self.engine) as session:
            dto = session.scalar(stmt)
        return None if dto is None else self.dto_to_mediated(dto)
