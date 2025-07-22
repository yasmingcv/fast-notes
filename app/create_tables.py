from app.database import engine, Base
from app.domain.entities import User

def create_tables():
    """Criar a tabela User"""
    Base.metadata.create_all(bind=engine)
    print("✅ Tabela User criada com sucesso!")

if __name__ == "__main__":
    create_tables()
