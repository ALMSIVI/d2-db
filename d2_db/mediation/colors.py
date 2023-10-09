from pydantic import BaseModel


class Color(BaseModel):
    transform_color: str
    code: str
