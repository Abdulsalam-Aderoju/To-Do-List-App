# Import Necessary Modules and classes
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import Operation, OperationStatus, OperationTitle, OperationDescription, ShowOperation, ShowStatus
from database import get_db
from models import Mission
from typing import List


# Create an APIRouter instance with a prefix and tags
router = APIRouter(prefix= "/missions", tags= ["Missions"])


# Define a route to handle HTTP POST requests to create a new mission
@router.post("/create")
def create_mission(request: Operation, db: Session = Depends(get_db)):
    
    # Create a new 'Mission' object using data from the 'request' object
    new_mission = Mission(title = request.title, description = request.description, user_id = request.user_id)
    
    # Add the new mission to the database
    db.add(new_mission)
    db.commit()
    db.refresh(new_mission)
    return "Mission was succesfully created!!"


@router.get("/", response_model= List[ShowOperation])
def all_missions(db: Session = Depends(get_db)):
    missions = db.query(Mission).all()
    
    if not missions:
        raise HTTPException(status_code= 404, detail= "You have not created any mission yet")
    else:
        return missions

@router.get("/{id}", response_model= ShowOperation)
def specific_mission(id, db: Session = Depends(get_db)):
    a_mission = db.query(Mission).filter(Mission.id == id).first()
    
    if not a_mission:
        raise HTTPException(status_code= 404, detail= "This mission does not exist")
    else:
        return a_mission
    
    


@router.put("/{id}/title")
def update_mission_title(id, request: OperationTitle, db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == id).first()

    if not mission:
        raise HTTPException(status_code= 404, detail= "This mission does not exist")
    else:
        Mission.title = request.title.title()
        db.commit()
        return f"Title of mission {id} has been successfully updated!!"
    


@router.put("/{id}/status")
def update_status(id, request: OperationStatus, db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == id).first()

    if not mission:
        raise HTTPException(status_code= 404, detail= f"Mission {id} doesn't exist")
    else:
        mission.status = request.status.title()
        db.commit()
        return f"Status of Mission {id} updated successfully!"
    

@router.put("/{id}/description")
def update_mission_description(id, request: OperationDescription, db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == id).first()

    if not mission:
        raise HTTPException(status_code= 404, detail= "This mission does not exist")
    else:
        Mission.description = request.description
        db.commit()
        return f"Description of mission {id} has been successfully updated!!"



@router.delete("/{id}/delete")
def delete_mission(id, db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == id).delete(synchronize_session= False)
    db.commit()

    if not mission:
        raise HTTPException(status_code= 404, detail= f"Mission {id} doesn't exist")
    
    else:
        return f"Mission {id} has been succesfully aborted!!"
    



