#!/bin/bash

# Configuração
PROJECT_NAME="taskmanager"
GIT_REPO="https://github.com/seu-usuario/taskmanager.git"
SERVER_IP="seu_ip_ou_dominio"
USER="seu_usuario"
PROJECT_DIR="/var/www/$PROJECT_NAME"

# Atualiza o sistema
echo "Atualizando o sistema..."
sudo apt update && sudo apt upgrade -y

# Instala dependências
echo "Instalando dependências..."
sudo apt install -y python3-pip python3-venv python3-dev python3-setuptools \
    build-essential libpq-dev postgresql postgresql-contrib nginx curl git

# Cria o usuário do sistema (se não existir)
if ! id "$USER" &>/dev/null; then
    sudo adduser --system --group --no-create-home $USER
fi

# Cria o diretório do projeto
sudo mkdir -p $PROJECT_DIR
sudo chown $USER:$USER $PROJECT_DIR

# Clona o repositório (se não existir)
if [ ! -d "$PROJECT_DIR/.git" ]; then
    git clone $GIT_REPO $PROJECT_DIR
fi

# Configura o ambiente virtual
if [ ! -d "$PROJECT_DIR/venv" ]; then
    python3 -m venv $PROJECT_DIR/venv
fi

# Ativa o ambiente virtual e instala as dependências
source $PROJECT_DIR/venv/bin/activate
pip install --upgrade pip
pip install -r $PROJECT_DIR/requirements.txt

# Configura o banco de dados
sudo -u postgres psql -c "CREATE DATABASE ${PROJECT_NAME}_prod;"
sudo -u postgres psql -c "CREATE USER ${PROJECT_NAME}_user WITH PASSWORD 'uma_senha_segura';"
sudo -u postgres psql -c "ALTER ROLE ${PROJECT_NAME}_user SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE ${PROJECT_NAME}_user SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE ${PROJECT_NAME}_user SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ${PROJECT_NAME}_prod TO ${PROJECT_NAME}_user;"

# Configura as variáveis de ambiente
if [ ! -f "$PROJECT_DIR/.env" ]; then
    cp $PROJECT_DIR/.env.example $PROJECT_DIR/.env
    # Gera uma nova chave secreta
    SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
    sed -i "s/SECRET_KEY=.*/SECRET_KEY='$SECRET_KEY'/" $PROJECT_DIR/.env
    # Atualiza as configurações do banco de dados
    sed -i "s/^DEBUG=.*/DEBUG=False/" $PROJECT_DIR/.env
    sed -i "s/^ALLOWED_HOSTS=.*/ALLOWED_HOSTS=$SERVER_IP,localhost/" $PROJECT_DIR/.env
    sed -i "s/^POSTGRES_DB=.*/POSTGRES_DB=${PROJECT_NAME}_prod/" $PROJECT_DIR/.env
    sed -i "s/^POSTGRES_USER=.*/POSTGRES_USER=${PROJECT_NAME}_user/" $PROJECT_DIR/.env
    sed -i "s/^POSTGRES_PASSWORD=.*/POSTGRES_USER=uma_senha_segura/" $PROJECT_DIR/.env
fi

# Aplica as migrações
python $PROJECT_DIR/manage.py migrate
python $PROJECT_DIR/manage.py collectstatic --noinput

# Configura o Gunicorn
GUNICORN_SERVICE="/etc/systemd/system/${PROJECT_NAME}.service"
sudo bash -c "cat > $GUNICORN_SERVICE << EOL
[Unit]
Description=gunicorn daemon for $PROJECT_NAME
After=network.target

[Service]
User=$USER
Group=www-data
WorkingDirectory=$PROJECT_DIR
ExecStart=$PROJECT_DIR/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:$PROJECT_DIR/$PROJECT_NAME.sock ${PROJECT_NAME}.wsgi:application

[Install]
WantedBy=multi-user.target
EOL"

# Configura o Nginx
NGINX_CONFIG="/etc/nginx/sites-available/$PROJECT_NAME"
sudo bash -c "cat > $NGINX_CONFIG << EOL
server {
    listen 80;
    server_name $SERVER_IP;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root $PROJECT_DIR;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:$PROJECT_DIR/$PROJECT_NAME.sock;
    }
}
EOL"

# Habilita o site e reinicia o Nginx
sudo ln -sf $NGINX_CONFIG /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Inicia o serviço do Gunicorn
sudo systemctl daemon-reload
sudo systemctl start $PROJECT_NAME
sudo systemctl enable $PROJECT_NAME

echo "\nDeploy concluído! Acesse http://$SERVER_IP"
