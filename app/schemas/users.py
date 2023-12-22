from schemas.base_model import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    password: str
    role: str


class UserModel(UserCreate):
    id: int
