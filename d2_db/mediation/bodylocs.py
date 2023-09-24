from pydantic import BaseModel


class BodyLoc(BaseModel):
    body_location: str
    code: str
