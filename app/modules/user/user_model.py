from sqlmodel import SQLModel, Field , select
from uuid import UUID, uuid4
from datetime import datetime
from ...utils.helper_functions import generate_timestamp
from ...utils.database import engine , Session
from hashlib import sha256


class UserBase(SQLModel):
    name: str
    image_url: str
    role: str
    age: int
    class_name: str
    email: str  
    password_hash: str  


class User(UserBase, table=True):
    __tablename__ = "users"  # Optional: Explicit table name
    user_id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=generate_timestamp)
    updated_at: datetime = Field(default_factory=generate_timestamp)

class UserDAO :
    
    def create_user(self, user:UserBase):
        with Session(engine) as session:
            hashed_password = sha256(user.password.encode()).hexdigest()
            db_user = User(
            name=user.name ,
            image_url=user.image_url ,
            role=user.role ,
            age=user.age ,
            class_name=user.class_name ,
            email=user.email ,
            password_hash= hashed_password
            )
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
        return db_user
    
    def get_all_users():
        with Session(engine) as session:
            users = session.exec(select(User)).all()
        return users
    
    def get_users_by_class( class_name:str):
        with Session(engine) as session:
            users = session.exec(select(User).where(User.class_name == class_name)).all()
        return users   
    
    def get_user_by_id( user_id: UUID):
        with Session(engine) as session:
            user = session.exec(select(User).where(User.user_id == user_id)).first()
            if not user:
                raise ValueError(f"User with ID {user_id} not found")
        return user
    
    def update_user( user_id:UUID , user:User):
        with Session(engine) as session:
            db_user = session.exec(select(User).where(User.user_id == user_id)).first()
            for key , value in user.model_dump().items():
                if value:
                    setattr(db_user , key , value)
            db_user.updated_at = generate_timestamp()
            session.commit()
            session.refresh(db_user)
        return db_user