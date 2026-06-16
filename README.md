# banco_api_mvc

Uma API bancária minimalista escrita em Python, criada como projeto de estudo e aplicação de portfólio. O objetivo principal é demonstrar organização em arquitetura MVC, clareza no design de código e a capacidade de implementar operações bancárias básicas (criação de contas, listagem, saques e extratos) usando MySQL como persistência principal.

**Status:** Projeto de estudo / portfólio — não destinado a produção.

**Principais pontos:**
- **Propósito:** Exibir habilidades de arquitetura, organização de código e testes básicos.
- **Arquitetura:** Model-View-Controller (MVC).
- **Persistência:** MySQL (container local via `docker-compose.yml` / esquema em `init/schema.sql`).

**Tecnologias:** Python, MySQL, SQLAlchemy.

**Estrutura do repositório (visão rápida para recrutadores)**

- **`run.py`**: Ponto de entrada para executar a API localmente. Veja [run.py](run.py).
- **`requirements.txt`**: Dependências do projeto. Veja [requirements.txt](requirements.txt).
- **`init/schema.sql`**: Script SQL para criar o esquema usado nos testes/desenvolvimento. Veja [init/schema.sql](init/schema.sql).
- **`src/`**: Código-fonte organizado por camadas:
	- **`src/controller/`**: Controladores que recebem requisições e coordenam respostas. Ex.: [src/controller/cpf_controller/cpf_create_account_controller.py](src/controller/cpf_controller/cpf_create_account_controller.py)
	- **`src/main/routes/`**: Definição de rotas da API. Ex.: [src/main/routes/cpf_routes.py](src/main/routes/cpf_routes.py)
	- **`src/models/mysql/`**: Repositórios, entidades e conexão que lidam com persistência (MySQL). Ex.: [src/models/mysql/repository/cpf_repository.py](src/models/mysql/repository/cpf_repository.py)
	- **`src/view/`**: Formatação das respostas HTTP (object -> response). Ex.: [src/view/cpf_view/cpf_create_account_view.py](src/view/cpf_view/cpf_create_account_view.py)

- **`tests/` / testes integrados e unitários:** Dentro de `src/` há arquivos de teste, por exemplo controllers e repositórios com sufixo `_test.py` (use `pytest` para rodar, caso instalado).

Como o repositório foi organizado para estudo, os nomes das pastas e arquivos seguem a separação por responsabilidade (controllers, composers, models, view, etc.), o que facilita a leitura e a avaliação técnica por recrutadores.

Guia rápido — executar localmente

1. Crie um ambiente virtual (recomendado):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Suba o banco MySQL local:

```bash
docker compose up -d mysql
```

4. Inicialize o esquema no banco:

```bash
mysql -h 127.0.0.1 -P 3306 -uroot -p bank_database < init/schema.sql
```

5. Execute a aplicação:

```bash
python run.py
```

Provavelmente a API ficará disponível em `http://localhost:3000`, na porta definida em `run.py`.

Observação: o acesso ao banco está configurado em [src/models/mysql/settings/connection.py](src/models/mysql/settings/connection.py), com a string de conexão apontando para o container MySQL local.

Execução de testes (se configurado):

```bash
pytest -q
```

Notas para recrutadores

- **Objetivo do projeto:** demonstrar organização de código, conhecimento de padrões (MVC) e prática com persistência local e testes.
- **Escopo:** implementação didática de operações bancárias (contas CPF/CNPJ, saques, extratos, listagens). Não contém autenticação, segurança ou preparação para produção.
- **O que avaliar:** clareza de separação de responsabilidades, estrutura de arquivos, uso de repositórios/entidades, e testes de unidade/integrados presentes.

