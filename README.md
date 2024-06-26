# Tech Challenge - Niuco Integration
Este projeto tem como objetivo integrar-se com a API de um SaaS utilizado por clientes da Niuco, extrair dados dos usuários através de endpoints REST e exibi-los de forma consolidada. A aplicação é desenvolvida em Python utilizando FastAPI.

## Descrição
A aplicação se conecta à API mock do SaaS, coleta dados dos usuários, converte-os conforme as regras especificadas e os exibe. 

## Estrutura de pastas 

challenge
  - Código-fonte principal da aplicação

tests
  - Testes automatizados garantindo a qualidade

.github
  - Pipeline de CI|CD

### Tecnologias utilizadas
- **Docker**: para desacoplamento de infraestrutura com uso de virtualização
- **Docker-compose**: Para orquestração da aplicação multi-container 
- **FastAPI**: framework web para a construção de APIs com Python
- **Pydantic**: Biblioteca de validação de código
- **Pytest**: para os testes unitários
- **Python**: utilizando o paradigma orientado a objetos
----------------------------------
### Instalação e Execução
Fiz utilizando WSL2 Ubuntu. 

Pré-requisitos
- Python 3.12.*
- Poetry
- pyenv
- Docker
- Docker-compose 


### Configurando o ambiente

1. Clone o repositório

```
git clone git@github.com:pedroarthuralvesdeoliveira/niuco.git
cd niuco
```
2. Configure o ambiente virtual usando pyenv: 
```
pyenv install 3.12.*
pyenv virtualenv 3.12.* niuco-integration
pyenv activate niuco-integration
```

3. Instale as dependências

```
poetry install
```


### Executando a aplicação

Primeiramente inicie a API mock: 
```
docker-compose up
```

Execute a aplicação (sem docker): 
```
task run
```

Execute a aplicação (com docker)
```
docker-compose up
```

### API
Com ambos os serviços executando, terá quatro endpoints: 
- users
- users/{id}
- formattedUsers
- formattedUsers/{id}

Com os seguintes payloads:

**users**

Request 

```
GET http://0.0.0.0:8000/users
```

Response 

```
[
  {
    "id": "1",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "last_activity": 1622499200,
    "role": "admin",
    "status": "enabled"
  },
  ...
]
```


**users/{id}**

Request 

```
GET http://0.0.0.0:8000/users/0373e634-2d03-457e-a24d-2b0c8c3b7c37
```

Response 

```
{
    "id": "0373e634-2d03-457e-a24d-2b0c8c3b7c37",
    "name": 'John Doe',
    "email": "john.doe@example.com",
    "last_activity": "1622499200",
    "role":'admin',
    "status":'enabled'
}
```

**formattedUsers**

Request 

```
GET http://0.0.0.0:8000/formattedUsers
```

Response 

```
[
  {
    "id": "0373e634-2d03-457e-a24d-2b0c8c3b7c37",
    "email": "jo****oe@example.com",
    "lastActivity": "2021-06-01T00:00:00Z"
  },
  ...
]
```


**formattedUsers/{id}**

Request 

```
GET http://0.0.0.0:8000/users/0373e634-2d03-457e-a24d-2b0c8c3b7c37
```

Response 

```
{
    "id": "0373e634-2d03-457e-a24d-2b0c8c3b7c37",
    "email": "jo****oe@example.com",
    "lastActivity": "2021-06-01T00:00:00Z",
}
```