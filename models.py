# Import Required Modules or Classes
from sqlalchemy import Column, String, Integer, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum



class CurrentStatus(Enum):
    yet_to_begin = "Yet To Begin"
    in_progress = "Currently In Progress"
    completed = "Completed"



class User(Base):
    __tablename__ = "users"

    # Column in table
    id = Column(Integer, primary_key=True, index= True)
    name = Column(String(30))
    email = Column(String(30))
    password = Column(String(90))

    #Mission Relationship(One user to Many missions)
    missions = relationship("Mission", back_populates= "user")


class Mission(Base):
    __tablename__ = "missions"

    # Columns in table
    id = Column(Integer, primary_key= True, index= True)
    title = Column(String(90))
    description = Column(String(80))
    status = Column(SQLAlchemyEnum(CurrentStatus), default= CurrentStatus.yet_to_begin, nullable= False)

    #User Relationship (Many missions to One user)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates= "missions") 

    #Task Relationship (One mission to Many tasks)
    tasks = relationship("Tasks", back_populates= "mission")



class Tasks(Base):
    __tablename__ = "tasks"

    #Columns in table
    id = Column(Integer, primary_key= True, index= True)
    name = Column(String(90))
    details = Column(String(80))
    status = Column(SQLAlchemyEnum(CurrentStatus), default= CurrentStatus.yet_to_begin, nullable = False)

    #Mission Relationship (Many tasks to One mission)
    mission_id = Column(Integer, ForeignKey("missions.id"))
    mission = relationship("Mission", back_populates= "tasks") #Relaionship: Class name and Column name





