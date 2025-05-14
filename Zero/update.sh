#!/bin/bash

# Atualiza o sistema
echo "Atualizando o sistema..."
sudo apt update && sudo apt upgrade -y

# Instala dependências do sistema
echo "Instalando dependências do sistema..."
sudo apt install -y python3-pip python3-venv python3-dev python3-setuptools \
    build-essential libpq-dev postgresql postgresql-contrib nginx curl

# Cria e ativa o ambiente virtual
echo "Criando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

# Instala as dependências do Python
echo "Instalando dependências do Python..."
pip install --upgrade pip
pip install -r requirements.txt

# Configura o banco de dados
echo "Configurando o banco de dados..."
sudo -u postgres psql -c "CREATE DATABASE taskmanager;"
sudo -u postgres psql -c "CREATE USER taskmanageruser WITH PASSWORD 'taskmanagerpass';"
sudo -u postgres psql -c "ALTER ROLE taskmanageruser SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE taskmanageruser SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE taskmanageruser SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE taskmanager TO taskmanageruser;"

# Aplica as migrações
echo "Aplicando migrações..."
python manage.py migrate

# Coleta arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "\nConfiguração concluída! Para iniciar o servidor, execute:"
echo "source venv/bin/activate"
echo "python manage.py runserver"
