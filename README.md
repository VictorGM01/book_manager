# Gerenciador de Livros com Django e PostgreSQL

## Descrição do Projeto
Sistema web para gerenciamento e catalogação de livros, possibilitando o armazenamento
destes livros em um banco de dados PostgreSQL e facilitando a vida das pessoas que, como nós ([Victor](https://github.com/VictorGM01)
e [Rapha](https://github.com/raphaelaferraz)), não possuem muito controle sobre seus livros 😅

Foi utilizado, para back-end, o banco de dados PostgreSQL e o framework Django com a linguagem de programação Python e, para o front-end, HTML5 e CSS.

<h1 align="center">
    <img src="https://img.shields.io/static/v1?label=DJANGO&message=FRAMEWORK&color=brightgreen&style=for-the-badge&logo=DJANGO&logoColor=green"/>
    <img src="https://img.shields.io/static/v1?label=POSTGRESQL&message=10.9.1&color=purple&style=for-the-badge&logo=POSTGRESQL&logoColor=purple"/>
    <img src="https://img.shields.io/static/v1?label=PYTHON&message=3.9.9&color=blue&style=for-the-badge&logo=Python"/>
    <img src="https://img.shields.io/static/v1?label=DJANGO&message=4.0.1&color=green&style=for-the-badge"/>
</h1>

## Status do Projeto :warning:
#### 🚧 👷🏻‍♂️ Em construção... 👷🏻‍♀️ 🚧

## Pré Requisitos
Antes de começar, é preciso que você tenha instalado na sua máquina as seguintes ferramentas:

[Git](https://git-scm.com/), [Python3](https://www.python.org/downloads/release/python-390/), [PostgreSQL](https://www.postgresql.org/download/windows/)

Além disso, é interessante instalar uma IDE para conseguir rodar a aplicação de maneira simplificada. Recomendo o uso do [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) ou do [VSCode](https://code.visualstudio.com/download)

## Como rodar a aplicação ▶
### Instalar o Framework django e dependências
````bash
# No termnial, crie uma venv:
python -m venv ./venv

# Depois de criada, ative-a digitando no terminal (WINDOWS):
venv\Scripts\activate

# Depois de criada, ative-a digitando no terminal (MAC ou LINUX):
source /venv/bin/activate

# Instale o Django com pip install
pip install django
````

### Configurar Banco de Dados
Após instalar o banco de dados, conforme solicitado em [Pré Requisitos](#pré-requisitos), crie um servidor chamado livros:

- Clique com o botão direito em 'Servidores':
![pgadmin.png](assets/img/pgadmin.png)
- Clique em Create e depois em Server:
![createserver.png](assets/img/createserver.png)
- Uma nova janela será aberta. Defina o nome como 'livros'. Em "Connection", defina o host como localhost e em password coloque a senha do seu PostgreSQL:
![connection.png](assets/img/connection.png)
- Após Criar o servidor, clique com o botão direito em databases e crie um:
![createdatabase.png](assets/img/createdatabase.png)
- Defina o nome do database como 'book_manager':
![databasename.png](assets/img/databasename.png)

### Configurando conexão com o banco de dados
De volta ao terminal, instale as dependências necessárias:
````bash
# Instale o módulo psycopg2
pip install psycopg2

# Instale o módulo psycopg2-binary
pip install psycopg2-binary
````

- Abra o arquivo settings.py, na pasta gerenciador_de_livros
- Na linha 71, substitua USER pelo nome do seu usuário do servidor do PostgreSQL (para verificar o nome, abra o postgresql novamente, clique com o botão direito do mouse sobre o servidor que você criou (livros), clique em properties e depois em connection):
![linha71.png](assets/img/linha71.png)
Obs.: Geralmente, o seu código deverá ficar assim: 'USER': 'postgres'
- Na linha 72, substitua PASSWORD pela sua senha do postreSQL:
![linha72.png](assets/img/linha72.png)
Ex.: 'PASSWORD': 'senhadedemonstracao'

### Criar Django-admin
No terminal, siga os seguintes passos:
````bash
# Crie um superuser
python manage.py createsuperuser

# Digite o seu nome de administrador, crie e confirme sua senha e insira seu e-mail nos campos indicados
````


## Desenvolvedores :octocat:
<table>
    <tr>
    <td align="center"><a href="https://github.com/VictorGM01"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/86068797?v=4" width="100px;" alt=""/><br /><sub><b>Victor G. Marques</b></sub></a><br /><a href="https://github.com/VictorGM01" title="Victor">👨‍🚀💻</a></td>
    <td align="center"><a href="https://github.com/raphaelaferraz"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/86068799?v=4" width="100px;" alt=""/><br /><sub><b>Raphaela G. Ferraz</b></sub></a><br /><a href="https://github.com/raphaelaferraz" title="Raphaela">👨‍🚀💻</a></td>
    </tr>
</table>