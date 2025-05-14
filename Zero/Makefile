.PHONY: help install test lint format clean run shell migrate createsuperuser

help:
	@echo "Available commands:"
	@echo "  make install     - Instala as dependências do projeto"
	@echo "  make test        - Executa os testes"
	@echo "  make lint        - Executa a análise estática do código"
	@echo "  make format      - Formata o código automaticamente"
	@echo "  make clean       - Remove arquivos gerados"
	@echo "  make run         - Inicia o servidor de desenvolvimento"
	@echo "  make shell       - Abre o shell do Django"
	@echo "  make migrate     - Aplica as migrações"
	@echo "  make createsuperuser - Cria um superusuário"

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest

lint:
	pylint --load-plugins=pylint_django taskmanager tasks

format:
	black .
	isort .

clean:
	find . -type d -name "__pycache__" -exec rm -r {} \;
	find . -type d -name ".pytest_cache" -exec rm -r {} \;
	rm -rf .coverage htmlcov

run:
	python manage.py runserver

shell:
	python manage.py shell

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser
