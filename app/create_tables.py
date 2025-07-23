from app.database import engine, Base
from app.domain.entities import User, Note, File, Access

def create_tables():
    """Criar as tabelas User, Note, File e Access"""
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas User, Note, File e Access criadas com sucesso!")

if __name__ == "__main__":
    create_tables()
