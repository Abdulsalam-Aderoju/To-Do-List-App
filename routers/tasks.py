from fastapi import APIRouter, Depends, HTTPException
from schemas import Todo, TodoName, TodoStatus, TodoDetails
from sqlalchemy.orm import Session
from database import get_db
from models import Tasks

router = APIRouter(prefix= "/tasks", tags= ["Tasks"])

@router.post("/")
def create_task(request: Todo, db: Session = Depends(get_db)):
    new_task = Tasks(name = request.name, details = request.details, mission_id = request.mission_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return "Task was successfully created!!"


@router.get("/{id}")
def specific_task(id, db: Session = Depends(get_db)):
    a_task = db.query(Tasks).filter(Tasks.id == id).first()
    
    if not a_task:
        raise HTTPException(status_code= 404, detail= f"Task {id} does not exist")
    else:
        return a_task
        

@router.put("/{id}/name")
def update_task_name(id, request: TodoName, db: Session = Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == id).first()

    if not task:
        raise HTTPException(status_code= 404, detail= "This task does not exist")
    else:
        task.name = request.name.title()
        db.commit()
        return f"Title of task {id} has been successfully updated!!"
    
@router.put("/{id}/details")
def update_task_details(id, request: TodoDetails, db: Session = Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == id).first()

    if not task:
        raise HTTPException(status_code= 404, detail= "This task does not exist")
    else:
        task.details = request.details
        db.commit()
        return f"Details of task {id} has been successfully updated!!"
    

@router.put("/{id}/status")
def update_task_status(id, request: TodoStatus, db: Session = Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == id).first()

    if not task:
        raise HTTPException(status_code= 404, detail= "This task does not exist")
    else:
        task.status = request.status.title()
        db.commit()
        return f"Status of task {id} has been successfully updated!!"

        
@router.delete("/{id}")
def delete_task(id, db: Session = Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.id == id).delete(synchronize_session= False)
    db.commit()

    if not task:
        raise HTTPException(status_code= 404, detail= f"Task {id} doesn't not exist in this mission")
    else:
        return f"Task {id} has been successfully abolished"