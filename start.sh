#!/bin/bash

# Script de inicialização do container
echo "🚀 Iniciando aplicação..."

# Aguardar banco estar disponível
echo "⏳ Aguardando banco de dados..."
until python -c "
import os
import psycopg2
import time

max_retries = 30
retry_count = 0

while retry_count < max_retries:
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'database'),
            port=os.getenv('DB_PORT', '5432'),
            user=os.getenv('DB_USER', 'fastnotes'),
            password=os.getenv('DB_PASSWORD', '1234'),
            database=os.getenv('DB_NAME', 'fastnotes_db')
        )
        conn.close()
        print('✅ Banco conectado!')
        break
    except psycopg2.OperationalError:
        retry_count += 1
        print(f'🔄 Tentativa {retry_count}/{max_retries}...')
        time.sleep(2)
else:
    print('❌ Não foi possível conectar ao banco!')
    exit(1)
"; do
  echo "🔄 Tentando novamente em 2 segundos..."
  sleep 2
done

# Criar tabelas automaticamente
echo "📋 Criando tabelas no banco..."
python app/create_tables.py

# Iniciar aplicação
echo "🎯 Iniciando FastAPI..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
