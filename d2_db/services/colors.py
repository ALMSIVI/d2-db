from sqlalchemy import select
from sqlalchemy.orm import Session

from d2_db.dto import ColorDTO
from d2_db.mediation import Color
from .__base__ import BaseService


class ColorService(BaseService[ColorDTO, Color]):
    __txt__ = 'colors.txt'

    def dto_from_txt(self, row, index: int):
        return ColorDTO(id=index, transform_color=row['Transform Color'], code=row['Code'])

    def dto_to_mediated(self, dto: ColorDTO) -> Color:
        return Color(transform_color=dto.transform_color, code=dto.code)

    def create_table(self):
        ColorDTO.metadata.create_all(self.engine)

    def find_by_id(self, color_id: int) -> Color | None:
        with Session(self.engine) as session:
            dto = session.get(ColorDTO, color_id)

        return None if dto is None else self.dto_to_mediated(dto)

    def find_by_code(self, code: str) -> Color | None:
        stmt = select(ColorDTO).where(ColorDTO.code == code)
        with Session(self.engine) as session:
            dto = session.scalar(stmt)
        return None if dto is None else self.dto_to_mediated(dto)
