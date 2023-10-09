from pydantic import BaseModel


class PlayerClass(BaseModel):
    player_class: str
    code: str
