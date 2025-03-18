from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime
from enum import Enum

class CreateUser(BaseModel):
    name: str
    image_url: str
    role: str
    age: int
    class_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    user_id: UUID
    name: str
    image_url: str
    role: str
    age: int
    class_name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime  # Corrected typo

class UpdateUser(BaseModel):
    name: Optional[str]
    image_url: Optional[str]
    role: Optional[str]
    age: Optional[int]
    class_name: Optional[str]
    email: Optional[EmailStr]
    password_hash: Optional[str]  
    

class UserRole(str , Enum):
    admin = "admin"
    student = "student"
    teacher = "teacher"