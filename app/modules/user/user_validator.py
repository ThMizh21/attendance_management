from fastapi import HTTPException, status
from uuid import UUID
from sqlmodel import select
from ...utils.database import Session, engine
from ..user.user_model import User
import string

class UserValidator:
    
    @staticmethod
    def email_validator(email: str):
        # Basic email format validation
        if "@" not in email or "." not in email.split("@")[-1]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format"
            )
        
        # Check if the email is unique
        with Session(engine) as session:
            existing_user = session.exec(select(User).where(User.email == email)).first()
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email is already in use"
                )
    
    @staticmethod
    def password_validator(password: str):
        if len(password) < 8:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 8 characters long"
            )
        
        if not any(char.isdigit() for char in password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must contain at least one digit"
            )
        if not any(char.islower() for char in password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must contain at least one lowercase letter"
            )
        
        if not any(char.isupper() for char in password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must contain at least one uppercase letter"
            )
        
        if not any(char in string.punctuation for char in password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must contain at least one special character"
            )
            
    @staticmethod
    def user_id_validator(user_id: UUID):
        with Session(engine) as session:
            existing_user = session.exec(select(User).where(User.user_id == user_id)).first()
            if not existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User ID not found"
                )