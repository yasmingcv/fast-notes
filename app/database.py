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
# a engine é responsável por estabelecer a conexão com o banco de dados
# e executar as operações de CRUD
engine = create_engine(DATABASE_URL)

# Criar SessionLocal class para sessões de banco
# cria sessões que serão usadas para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class para modelos
# é uma classe usada para todos os modelos/entidades do banco de dados
Base = declarative_base()

# Dependency para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        # aqui o yield é usada para entregar a sessão ao FastAPI
        # não usa-se return porque o FastAPI espera um gerador
        # que possa ser usado em várias requisições
        # se usasse o return, a sessão seria fechada imediatamente
        # e não poderia ser reutilizada
        # o que faria com que eu tivesse que abrir uma nova sessão a cada requisição
        # o que não é eficiente
        yield db
    finally:
        db.close()
