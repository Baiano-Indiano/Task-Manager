# Como Contribuir

Obrigado por considerar contribuir para o projeto! Aqui estão algumas diretrizes para ajudar você a começar.

## Configuração do Ambiente de Desenvolvimento

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/taskmanager.git
   cd taskmanager
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   # Linux/Mac
   python -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   # Edite o arquivo .env conforme necessário
   ```

5. **Aplique as migrações**
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Execute o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

## Padrões de Código

- Siga o [PEP 8](https://www.python.org/dev/peps/pep-0008/) para código Python
- Use [Black](https://github.com/psf/black) para formatação automática
- Use [isort](https://pycqa.github.io/isort/) para organizar imports
- Escreva docstrings seguindo o [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

## Fluxo de Trabalho

1. Crie uma branch para sua feature/correção:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

2. Faça commit das suas alterações:
   ```bash
   git add .
   git commit -m "Adiciona nova funcionalidade"
   ```

3. Envie suas alterações para o repositório remoto:
   ```bash
   git push origin feature/nova-funcionalidade
   ```

4. Abra um Pull Request (PR) para a branch `main`

## Testes

Certifique-se de que todos os testes passem antes de enviar um PR:

```bash
pytest
```

## Relatando Problemas

Ao relatar um problema, por favor inclua:

1. Descrição clara e concisa do problema
2. Passos para reproduzir o problema
3. Comportamento esperado
4. Comportamento atual
5. Capturas de tela (se aplicável)
6. Versão do Python, Django e outras dependências relevantes

## Código de Conduta

Este projeto segue o [Código de Conduta do Contribuidor](CODE_OF_CONDUCT.md). Ao participar, espera-se que você siga este código.

## Agradecimentos

Obrigado por sua contribuição! Sua ajuda é muito apreciada.
