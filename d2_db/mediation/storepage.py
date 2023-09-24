from pydantic import BaseModel


class StorePage(BaseModel):
    store_page: str
    code: str
