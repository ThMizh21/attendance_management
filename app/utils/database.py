from sqlmodel import create_engine , Session , SQLModel

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL ,echo =True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
__all__ =[engine ,Session]