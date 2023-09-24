from typing import Any

from sqlalchemy.orm import Session

from d2_db.dto import EventDTO
from d2_db.mediation import Event
from .__base__ import BaseService


class EventService(BaseService[EventDTO, Event]):
    __txt__ = 'events.txt'

    def dto_from_txt(self, row: dict[str, Any], index: int) -> EventDTO:
        return EventDTO(event=row['event'], description=row['*description'])

    def dto_to_mediated(self, dto: EventDTO) -> Event:
        return Event(event=dto.event, description=dto.description)

    def create_table(self):
        EventDTO.metadata.create_all(self.engine)

    def find_by_event(self, event: str) -> Event | None:
        with Session(self.engine) as session:
            dto = session.get(EventDTO, event)

        return None if dto is None else self.dto_to_mediated(dto)
