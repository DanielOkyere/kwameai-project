from pydantic import BaseModel


class Postcreate(BaseModel):
    title: str
    content: str
    published: bool
    image: str


class Postupdate(Postcreate):
    title: str | None
    content: str | None
    published: bool | None
    image: str | None


class Post(Postcreate):
    id: int
    title: str | None
    content: str | None
    published: str | None
    image: str | None

    class Config:
        orm_mode = True
