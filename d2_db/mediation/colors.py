from pydantic import BaseModel


class Color(BaseModel):
    id: int
    transform_color: str
    code: str
