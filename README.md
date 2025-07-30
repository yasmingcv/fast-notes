# 🚀 Fast Notes API

Uma API moderna e robusta para gerenciamento de notas pessoais com autenticação JWT, upload de arquivos para AWS S3 e arquitetura limpa baseada em FastAPI.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Funcionalidades

- 🔐 **Autenticação JWT** - Sistema completo de login com tokens seguros
- 📝 **Gerenciamento de Notas** - CRUD completo para notas pessoais
- 📁 **Upload de Arquivos** - Integração com AWS S3 para anexos
- 👤 **Gestão de Usuários** - Registro, atualização e controle de perfis
- 🔒 **Autorização** - Cada usuário acessa apenas suas próprias notas
- 📚 **Documentação Automática** - Swagger UI e ReDoc integrados
- 🐳 **Docker Ready** - Containerização completa com docker-compose
- 🔧 **Arquitetura Limpa** - Separação clara entre domínio, serviços e apresentação

## 🛠️ Tecnologias Utilizadas

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e de alta performance
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Validação de dados e serialização
- **[SQLAlchemy](https://sqlalchemy.org/)** - ORM poderoso para Python
- **[PostgreSQL](https://postgresql.org/)** - Banco de dados relacional robusto
- **[Uvicorn](https://uvicorn.org/)** - Servidor ASGI de alta performance

### Autenticação & Segurança
- **[PyJWT](https://pyjwt.readthedocs.io/)** - JSON Web Tokens para autenticação
- **[bcrypt](https://pypi.org/project/bcrypt/)** - Hash seguro de senhas
- **[python-multipart](https://pypi.org/project/python-multipart/)** - Suporte a formulários multipart

### Cloud & Storage
- **[Boto3](https://boto3.amazonaws.com/)** - SDK oficial da AWS
- **[AWS S3](https://aws.amazon.com/s3/)** - Storage de arquivos na nuvem

## 🏗️ Arquitetura

```
app/
├── 📁 domain/           # Entidades e schemas do domínio
│   ├── entities/        # Modelos SQLAlchemy
│   └── schemas/         # Schemas Pydantic
├── 📁 services/         # Lógica de negócio
├── 📁 repositories/     # Acesso a dados
├── 📁 routers/          # Endpoints da API
├── 📁 auth/             # Sistema de autenticação
├── 📁 utils/            # Utilitários (bcrypt, jwt)
└── 📄 database.py       # Configuração do banco
```

## 🚀 Como Executar

### Pré-requisitos
- Docker e Docker Compose
- Conta AWS (para S3)

### 1. Clone o repositório
```bash
git clone https://github.com/yasmingcv/fast-notes
cd fast-notes
```

### 2. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

### 3. Execute com Docker
```bash
# Subir toda a aplicação
docker-compose up --build

# Em background
docker-compose up --build -d
```

### 4. Acesse a aplicação
- **API**: http://localhost:8000
- **Documentação**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📋 Variáveis de Ambiente

```env
# Database
DB_USER=fastnotes
DB_PASSWORD=1234
DB_NAME=fastnotes_db
DB_HOST=database
DB_PORT=5432

# AWS Credentials
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1
BUCKET_NAME=your-bucket-name

# Application
DEBUG=True
SECRET_KEY=your_secret_key
SECRET_KEY_JWT=your_jwt_secret
```

## 📖 Endpoints Principais

### 👤 Usuários
- `POST /users/` - Criar usuário
- `PUT /users/me` - Atualizar perfil do usuário logado

### 🔐 Autenticação
- `POST /auth/login` - Login

### 📝 Notas
- `GET /notes/` - Listar minhas notas
- `POST /notes/` - Criar nota
- `GET /notes/{id}` - Buscar nota por ID
- `PUT /notes/{id}` - Atualizar nota
- `DELETE /notes/{id}` - Deletar nota

### 📁 Arquivos
- `POST /files/upload` - Upload de arquivo


## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/amazing-feature`)
3. Commit suas mudanças (`git commit -m 'Add some amazing feature'`)
4. Push para a branch (`git push origin feature/amazing-feature`)
5. Abrir um Pull Request

## 👨‍💻 Autora

Desenvolvido por [Yasmin Gonçalves](https://github.com/yasmingcv)

---

⭐ **Se este projeto te ajudou, considere dar uma estrela!** ⭐