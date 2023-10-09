from pydantic import BaseModel


class Composit(BaseModel):
    name: str
    token: str
