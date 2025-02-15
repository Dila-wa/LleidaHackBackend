import glob
from fastapi import HTTPException

from models.LleidaHacker import LleidaHacker as ModelLleidaHacker

from schemas.LleidaHacker import LleidaHacker as SchemaLleidaHacker

from security import get_password_hash

from sqlalchemy.orm import Session

def checkImage(imageId:str):
    return glob.glob("static/"+imageId+".*")

async def get_all(db: Session):
    return db.query(ModelLleidaHacker).all()

async def get_lleidahacker(userId: int, db: Session):
    return db.query(ModelLleidaHacker).filter(ModelLleidaHacker.id == userId).first()

async def add_lleidahacker(payload: SchemaLleidaHacker, db: Session):
    # if not checkImage(payload.image_id):
        # raise HTTPException(status_code=400, detail="Image not found")
    new_lleidahacker = ModelLleidaHacker(name=payload.name,
                                         email=payload.email,
                                         password=get_password_hash(payload.password),
                                         nickname=payload.nickname,
                                         birthdate = payload.birthdate,
                                         food_restrictions=payload.food_restrictions,
                                         telephone=payload.telephone,
                                         address=payload.address,
                                         shirt_size=payload.shirt_size,
                                         nif=payload.nif,
                                         student=payload.student,
                                         role=payload.role,
                                         #   group=payload.group,
                                         active=payload.active,
                                         image_id=payload.image_id,
                                         github=payload.github,
                                        #  linkdin=payload.linkdin,
    )
    db.add(new_lleidahacker)
    db.commit()
    db.refresh(new_lleidahacker)
    return new_lleidahacker

async def update_lleidahacker(userId: int, payload: SchemaLleidaHacker, db: Session):
    checkImage(lleidahacker.image_id)
    lleidahacker = db.query(ModelLleidaHacker).filter(ModelLleidaHacker.id == userId).first()
    lleidahacker.name = payload.name
    lleidahacker.email = payload.email
    lleidahacker.password = payload.password
    lleidahacker.nickname = payload.nickname
    lleidahacker.birthdate = payload.birthdate
    lleidahacker.food_restrictions = payload.food_restrictions
    lleidahacker.telephone = payload.telephone
    lleidahacker.address = payload.address
    lleidahacker.shirt_size = payload.shirt_size
    lleidahacker.nif = payload.nif
    lleidahacker.student = payload.student
    lleidahacker.role = payload.role
    lleidahacker.group = payload.group
    lleidahacker.active = payload.active
    lleidahacker.image_id = payload.image_id
    lleidahacker.github = payload.github
    db.commit()
    db.refresh(lleidahacker)
    return lleidahacker

async def delete_lleidahacker(userId: int, db: Session):
    lleidahacker = db.query(ModelLleidaHacker).filter(ModelLleidaHacker.id == userId).first()
    db.delete(lleidahacker)
    db.commit()
    return lleidahacker
