from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



DATABASE_URL = "mysql://root:ishola2020@localhost:3306/todo"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind= engine, autocommit = False, autoflush= False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


