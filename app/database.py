import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Variáveis do banco de dados
DB_USER = os.getenv("DB_USER", "fastnotes")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
DB_NAME = os.getenv("DB_NAME", "fastnotes_db")
DB_HOST = os.getenv("DB_HOST", "database") 
DB_PORT = os.getenv("DB_PORT", "5432")

# Construir URL do banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Criar SessionLocal class para sessões de banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class para modelos
Base = declarative_base()

# Dependency para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
