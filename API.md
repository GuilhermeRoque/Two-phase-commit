# Documentação da API do Web Service

> O documento descreve API REST do Serviço Web. 


## Contas

Endpoint: **`/accounts`**


#### GET /accounts
Retorna um documento JSON com as contas e seus respectivos saldos.

* **Código  de resposta de sucesso:**`200 OK`

* **Corpo da resposta:**

  ```json{
  "accounts": [
    {
      "balance": 500,
      "id": 1
    },
    {
      "balance": 1500,
      "id": 2
    },
    {
      "balance": 500,
      "id": 3
    },
    {
      "balance": 1500,
      "id": 4
    }
  ]
}```

Endpoint: **`/replicas`**


#### GET /replicas
Retorna um documento JSON com o endpoint de cada réplica, além de seu identificador único.

* **Código  de resposta de sucesso:**`200 OK`

* **Corpo da resposta:**

  ```json{
{
  "replicas": [
    {
      "endpoint": "http://192.168.0.15/pp02",
      "id": "replica3"
    },
    {
      "endpoint": "http://192.168.0.1/pp02",
      "id": "replica4"
    }
  ]
}
```


#### POST /replicas
Recebe um documento JSON com o endpoint de cada réplica, além de seu identificador único.
* **Código  de resposta de sucesso:**`201 CREATED`

* **Corpo da requisição:**

  ```json{
{
  "replicas": [
    {
      "endpoint": "http://192.168.0.15/pp02",
      "id": "replica3"
    },
    {
      "endpoint": "http://192.168.0.1/pp02",
      "id": "replica4"
    }
  ]
}


* **Corpo da resposta:**

  ```json{
{
  "replicas": [
    {
      "endpoint": "http://192.168.0.15/pp02",
      "id": "replica3"
    },
    {
      "endpoint": "http://192.168.0.1/pp02",
      "id": "replica4"
    }
  ]
}
```
#### DELETE /replicas
Recebe um documento JSON com o endpoint de cada réplica, além de seu identificador único.
* **Código  de resposta de sucesso:**`201 CREATED`

* **Corpo da requisição:**

  ```json{
{
  "replicas": [
    {
      "endpoint": "http://192.168.0.15/pp02",
      "id": "replica3"
    },
    {
      "endpoint": "http://192.168.0.1/pp02",
      "id": "replica4"
    }
  ]
}```
