from pydantic import BaseModel


class PlayerClass(BaseModel):
    id: int
    player_class: str
    code: str
