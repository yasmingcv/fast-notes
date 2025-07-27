from typing import Type, TypeVar, Generic, Optional, List
from sqlalchemy.orm import Session
from pydantic import BaseModel

ModelType = TypeVar("ModelType")  # Tipo da entidade (ex: Note)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)  # Tipo do Pydantic de criação

class BaseRepository(Generic[ModelType, CreateSchemaType]):
    def __init__(self, db: Session, model: Type[ModelType]):
        self.db = db
        self.model = model

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.dict())
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get(self, id: int) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def list_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def update(self, id: int, obj_in: CreateSchemaType) -> Optional[ModelType]:
        db_obj = self.get(id)
        if not db_obj:
            return None
        for key, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, key, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> Optional[ModelType]:
        db_obj = self.get(id)
        if not db_obj:
            return None
        self.db.delete(db_obj)
        self.db.commit()
        return db_obj
