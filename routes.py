from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db

router = APIRouter()

@router.post("/create_configuration", response_model=schemas.ConfigurationRead)
def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_configuration(db, config)

@router.get("/get_configuration/{country_code}", response_model=schemas.ConfigurationRead)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.post("/update_configuration", response_model=schemas.ConfigurationRead)
def update_configuration(config: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.update_configuration(db, config)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.delete("/delete_configuration/{country_code}")
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.delete_configuration(db, country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return {"message": "Configuration deleted successfully"}