# banco_api_mvc
## Descrição do Projeto
Este projeto consiste em uma API (Application Programming Interface) desenvolvida em Python para simular operações bancárias básicas, como gerenciamento de contas e transações.

A aplicação foi desenvolvida seguindo o padrão de design Model-View-Controller (MVC), visando modularidade, organização e facilidade de manutenção.

## Arquitetura: Model-View-Controller (MVC)
A aplicação segue estritamente o padrão Model-View-Controller (MVC), que é um padrão arquitetural que separa a lógica da aplicação em três componentes principais, cada um com responsabilidades distintas:

Model (Modelo): É responsável pela lógica de negócios e pela manipulação dos dados. No contexto desta API, o Model lida com a conexão e persistência de dados no banco, executando operações como criação, leitura, atualização e exclusão (CRUD) de contas e transações.

View (Visão): Em uma API, a View não é uma interface gráfica, mas sim o componente que formata os dados para o cliente. É responsável por transformar os dados processados pelo Model em um formato de resposta padrão, geralmente JSON.

Controller (Controlador): Atua como o intermediário. Ele recebe as requisições HTTP do cliente, chama os métodos apropriados no Model para processar a lógica de negócios e, em seguida, utiliza a View para formatar a resposta que será enviada de volta ao cliente.

## Tecnologias Utilizadas
As tecnologias e ferramentas utilizadas no desenvolvimento deste projeto são:

Linguagem de Programação: Python

Banco de Dados: SQLite (indicado pelo arquivo bancomvc.db), um sistema de gerenciamento de banco de dados relacional leve e sem servidor.

Framework API: Um framework Python (inferido) para lidar com roteamento, requisições HTTP e estruturar a aplicação como uma API.

Gerenciamento de Dependências: requirements.txt.


# Como Executar
## Para iniciar a API localmente, siga os passos abaixo:

Clone o repositório:

- git clone https://github.com/Amilcar-Cesar/banco_api_mvc
- cd banco_api_mvc
- Instale as dependências: Certifique-se de ter o Python e o pip instalados.
- pip install -r requirements.txt
- Execute a Aplicação: python run.py

A API estará acessível no endereço e porta configurados no arquivo run.py (geralmente http://localhost:<PORTA>).
