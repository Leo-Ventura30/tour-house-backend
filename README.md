
# Teste back-end - Tour House


#### Requisitos:
- python=3.11
- docker
- docker-compose

### Como buildar e upar o servidor

```
$ docker-compose build
$ docker-compose up
```

### Executando migrações
```
$ docker exec -it tour_house_management_web_1 sh
$ python manage.py makemigrations
```

### Criando superuser
```
$ python manage.py createsuperuser
```


### Autenticação e Permissões
##### Necessário criar usuário pelo admin
- curl ou httpie

#### request
para ter acesso a api basta ter o token de acesso ou logar pelo terminal.
```
$ http post :8000/api/login/ username=root password=root #usuário criado no admin
```
#### response
```
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 52
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Wed, 15 Mar 2023 17:26:55 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.2
Vary: Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "token": "5f175d17e6bb35247aec12fd21cb05f35785379e"
}
```

Para acessar qaulquer rota da API basta incluir o token gerado.
```
http get :8000/api/{path}/ 'authorization: token 5f175d17e6bb35247aec12fd21cb05f35785379e'
```
    
### API

Consultor

    Logar como consultor ou admin: POST /Login

Empresas

    Listar empresas cadastradas: GET /companies
    Consultar detalhes de uma empresa: GET /companies/{id}
    Criar nova empresa: POST /companies
    Atualizar dados de uma empresa: PUT /companies/{id}
    Inativar uma empresa: DELETE /companies/{id}

Departamentos

    Listar departamentos cadastrados: GET /departments
    Consultar detalhes de um departamento: GET /departments/{id}
    Criar novo departamento: POST /departments
    Atualizar dados de um departamento: PUT /departments/{id}
    Inativar um departamento: DELETE /departments/{id}

Funcionários

    Listar funcionários cadastrados: GET /employees
    Consultar detalhes de um funcionário: GET /employees/{id}
    Criar novo funcionário: POST /employees
    Atualizar dados de um funcionário: PUT /employees/{id}
    Inativar um funcionário: DELETE /employees/{id}

Provedor

    Listar provedores cadastrados: GET /provider
    Consultar detalhes de um provedor: GET /provider/{id}
    Criar novo provedor: POST /provider
    Atualizar dados de um provedor: PUT /provider/{id}
    Inativar um provedor: DELETE /provider/{id}

Integração com ERP

    Integrar funcionários ao ERP: POST /integracao/erp/employees
    Exibir historico de integrações do ERP: GET /integracao/erp/employees
    Consultar o historico detalho da integração: GET /integracao/erp/employees/{id}
    
### Visualização via Django Rest Framework
```
{
    "employees": "http://localhost:8000/api/employees/",
    "departments": "http://localhost:8000/api/departments/",
    "companies": "http://localhost:8000/api/companies/",
    "provider": "http://localhost:8000/api/provider/",
    "integracao/erp/employees": "http://localhost:8000/api/integracao/erp/employees/"
}
```
