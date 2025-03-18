from fastapi import APIRouter 
from .user_service import UserService
from .user_schema import CreateUser , UserResponse ,UpdateUser
from .user_model import User
from typing import List 
from uuid import UUID

rounter = APIRouter()

@rounter.get("/users" , response_model=List[UserResponse])
def get_all_users():
    return UserService.get_all_users()

@rounter.get("/users/class/{class_name}" , response_model=List[UserResponse])
def get_users_by_class(class_name:str):
    return UserService.get_users_by_class(class_name)

@rounter.get("/users/{user_id}" ,response_model= UserResponse )
def get_user_by_id(user_id:UUID):
    return UserService.get_user_by_id(user_id)

@rounter.post("/users/create-user/" ,)
def create_user(user:CreateUser):
    return UserService.create_user(user)

@rounter.put("/users/update-user/{user_id}")
def update_user(user_id:UUID , user:UpdateUser):
    return UserService.update_user(user_id , user)