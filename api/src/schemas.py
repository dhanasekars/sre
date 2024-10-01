from pydantic import BaseModel,EmailStr
from datetime import date
from typing import Optional

# Request schema for creating a student
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    date_of_birth: Optional[date] = None

    class Config:
        from_attributes = True


# Response schema for returning student data
class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    date_of_birth: Optional[date] = None

    class Config:
        from_attributes = True


class StudentUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    date_of_birth: Optional[date]