
# Imagem do Python 3.11 slim (imagem mais leve para melhor performance)
FROM python:3.11-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/code

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /code

# Copiar os requisitos do sistema
COPY ./requirements.txt /code/requirements.txt

# Instalar as dependências do Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /code/requirements.txt

# Copiar o código da aplicação e script de inicialização
COPY ./app /code/app
COPY ./start.sh /code/start.sh

# Dar permissão de execução ao script
RUN chmod +x /code/start.sh

# Expor a porta da aplicação
EXPOSE 8000

# Executar script de inicialização
CMD ["./start.sh"]