from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Tipos genéricos
EntityType = TypeVar("EntityType")  # Entidade SQLAlchemy (User, Note, etc.)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)  # Schema de criação
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)  # Schema de atualização
ResponseSchemaType = TypeVar("ResponseSchemaType", bound=BaseModel)  # Schema de resposta


class BaseService(Generic[EntityType, CreateSchemaType, UpdateSchemaType, ResponseSchemaType]):
    def __init__(self, repository_class: Type):
        self.repository_class = repository_class
        self.response_schema = None  # Será definido nas classes filhas

    def _get_repository(self, db: Session):
        return self.repository_class(db)

    # Adaptar a resposta para o schema definido
    def _to_response_schema(self, entity: EntityType) -> ResponseSchemaType:
        if not self.response_schema:
            raise NotImplementedError("response_schema deve ser definido na classe filha")
        return self.response_schema.model_validate(entity, from_attributes=True)

    def _to_response_list(self, entities: List[EntityType]) -> List[ResponseSchemaType]:
        return [self._to_response_schema(entity) for entity in entities]

    def create(self, db: Session, obj_create: CreateSchemaType) -> ResponseSchemaType:
        repo = self._get_repository(db)
        entity = repo.create(obj_create)
        return self._to_response_schema(entity)

    def get_by_id(self, db: Session, id: int) -> Optional[ResponseSchemaType]:
        repo = self._get_repository(db)
        entity = repo.get(id)
        if not entity:
            return None
        return self._to_response_schema(entity)

    def list_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ResponseSchemaType]:
        repo = self._get_repository(db)
        entities = repo.list_all(skip, limit)
        return self._to_response_list(entities)

    def update(self, db: Session, id: int, obj_update: UpdateSchemaType) -> Optional[ResponseSchemaType]:
        repo = self._get_repository(db)
        entity = repo.update(id, obj_update)
        if not entity:
            return None
        return self._to_response_schema(entity)

    def delete(self, db: Session, id: int) -> bool:
        repo = self._get_repository(db)
        return repo.delete(id)

    def count(self, db: Session) -> int:
        repo = self._get_repository(db)
        return repo.count()
