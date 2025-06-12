# Loja de Produtos

Este é um projeto de backend desenvolvido em Python com Flask, voltado para portfólio e apresentação. Ele simula uma API para cadastro, autenticação de usuários e gerenciamento de produtos, incluindo controle de permissões, CRUD de produtos por vendedores e visualização pública.

---

## Objetivo

> Projeto desenvolvido para fins de estudo, portfólio e demonstração de habilidades em desenvolvimento backend com Flask, JWT, SQLAlchemy e PostgreSQL.

---

## Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-Migrate
- Alembic
- SQLAlchemy
- PostgreSQL
- Passlib / bcrypt
- python-dotenv

(Consulte o arquivo [`requirements.txt`](./requirements.txt) para a lista completa de dependências.)

---

## Como rodar localmente

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Gui-SBarbosa/Loja-de-Produtos.git
   cd Loja-de-Produtos
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados PostgreSQL**
   - Certifique-se de ter uma instância do PostgreSQL em funcionamento.
   - Crie um banco de dados para o projeto.
   - Defina a variável de ambiente `SQLALCHEMY_DATABASE_URI` com sua string de conexão, por exemplo:  
     `postgresql://usuario:senha@localhost:5432/nome_do_banco`
   - Você pode adicionar essa variável no arquivo `.flaskenv` ou `.env` na raiz do projeto.

5. **Configure outras variáveis de ambiente**
   - Exemplo de `.flaskenv`:
     ```
     FLASK_APP=run.py
     FLASK_ENV=development
     SQLALCHEMY_DATABASE_URI=postgresql://usuario:senha@localhost:5432/nome_do_banco
     JWT_SECRET_KEY=sua_chave_secreta
     ```

6. **Inicialize o banco de dados**
   ```bash
   flask db upgrade
   python db_create.py
   ```

7. **Execute a aplicação**
   ```bash
   flask run
   ```

---

## Rotas da API

### Autenticação

- **POST `/register`**  
  Cadastra um novo usuário  
  Body: `name`, `email`, `password`, `role`  
  - 201: Usuário criado  
  - 400/409: Erro de validação ou email já existente

- **GET `/login`**  
  Realiza login do usuário  
  Body: `email`, `password`  
  - 200: Token JWT  
  - 400/401: Erro de autenticação

---

### Produtos

#### Protegidas (necessário login como SELLER)

- **POST `/products/create`**  
  Cria um produto

- **GET `/products/my`**  
  Lista produtos do vendedor autenticado

- **PUT `/products/<product_id>`**  
  Atualiza produto do vendedor autenticado

- **DELETE `/products/<product_id>`**  
  Remove produto do vendedor autenticado

#### Públicas

- **GET `/products/all`**  
  Lista todos os produtos cadastrados

- **GET `/products/details/<product_id>`**  
  Detalhes de um produto pelo ID

---

## Observações

- O projeto foi desenvolvido com foco em aprendizado e demonstração de boas práticas de API RESTful com Flask e PostgreSQL.
- Sinta-se à vontade para abrir Issues ou Pull Requests!

---