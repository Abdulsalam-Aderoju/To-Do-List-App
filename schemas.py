from pydantic import BaseModel
from typing import List


class Account(BaseModel):
    name: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str




class OperationBase(BaseModel):
    title: str
    description: str
    user_id: int

class Operation(OperationBase):
    class Config():
        orm_mode = True

class OperationTitle(BaseModel):
    title: str

class OperationDescription(BaseModel):
    description: str

class OperationStatus(BaseModel):
    status: str



class TodoBase(BaseModel):
    name: str
    details: str
    mission_id: int

class Todo(TodoBase):
    class Config():
        orm_mode = True


class TodoName(BaseModel):
    name: str

class TodoDetails(BaseModel):
    details: str

class TodoStatus(BaseModel):
    status: str



class ShowUser(BaseModel):
    name: str
    email: str
    missions: List[Operation] = []

    class Config():
        orm_mode = True



class ShowOperation(BaseModel):
    title: str
    description: str
    tasks: List[Todo] = []

    class Config():
        orm_mode = True

class ShowStatus(OperationStatus):
    class Config():
        orm_mode = True

