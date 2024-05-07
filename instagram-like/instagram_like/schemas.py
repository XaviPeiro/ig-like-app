from pydantic import BaseModel as BaseSchema


class UserBase(BaseSchema):
    email: str


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    images: list["Image"]

    class Config:
        orm_mode = True


class ImageBase(BaseSchema):
    name: str
    url: str
    owner_id: User


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True


class ImageDetail(ImageBase):
    ...
