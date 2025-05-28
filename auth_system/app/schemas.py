# app/schemas.py

from pydantic import BaseModel

# Request schema for user registration
class UserCreate(BaseModel):
    username: str
    password: str

# Request schema for login
class UserLogin(BaseModel):
    username: str
    password: str

# Response schema
class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True  # Needed for SQLAlchemy model compatibility

