from pydantic import BaseModel


class JSON(BaseModel):
    id_news: int
    id_user: int
    tags: str
    url: str
