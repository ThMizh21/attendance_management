from ...utils.database import engine , Session 
from .user_schema import *
from .user_model import UserBase ,User , UserDAO
from hashlib import sha256
from sqlmodel import select
from .user_validator import UserValidator

class UserService:
    
    def create_user( user:UserBase):
        UserValidator.email_validator(user.email)
        UserValidator.password_validator(user.password)
        return UserDAO().create_user(user)
        
    def get_all_users():
        return UserDAO.get_all_users()
    
    def get_users_by_class( class_name:str):
        return UserDAO.get_users_by_class(class_name)
    
    def get_user_by_id(user_id: UUID):
        UserValidator.user_id_validator(user_id)
        return UserDAO.get_user_by_id(user_id)
    
    def update_user( user_id:UUID , user:User):
        UserValidator.user_id_validator(user_id)
        UserValidator.email_validator(user.email)
        UserValidator.password_validator(user.password) 
        return UserDAO.update_user(user_id , user)
                       
            
            






