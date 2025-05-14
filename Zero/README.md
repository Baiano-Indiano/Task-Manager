# Gerenciador de Tarefas

Um simples gerenciador de tarefas desenvolvido com Django.

## Funcionalidades

- Listar todas as tarefas
- Adicionar nova tarefa
- Editar tarefa existente
- Excluir tarefa
- Marcar tarefa como concluída

## Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd nome-do-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   SECRET_KEY=sua_chave_secreta_aqui
   ```

5. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário (opcional, para acessar o painel de administração):
   ```bash
   python manage.py createsuperuser
   ```

7. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

8. Acesse a aplicação em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Acesso ao Painel de Administração

Para acessar o painel de administração, acesse [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e faça login com suas credenciais de superusuário.

## Estrutura do Projeto

- `taskmanager/`: Configurações do projeto Django
- `tasks/`: Aplicativo de gerenciamento de tarefas
  - `migrations/`: Migrações do banco de dados
  - `templates/tasks/`: Templates HTML
  - `admin.py`: Configuração do painel de administração
  - `forms.py`: Formulários
  - `models.py`: Modelos de dados
  - `urls.py`: URLs do aplicativo
  - `views.py`: Lógica de visualização
