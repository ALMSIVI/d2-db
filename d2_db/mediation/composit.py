from pydantic import BaseModel


class Composit(BaseModel):
    id: int
    name: str
    token: str
