# Documentação da API do Web Service

> O documento descreve API REST do Serviço Web. 


## Contas

Endpoint: **`/accounts`**


#### GET /accounts
Retorna um documento JSON com as contas e seus respectivos saldos.

* **Código  de resposta de sucesso:**`200 OK`

* **Corpo da resposta:**

  ```json
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

## Réplicas

Endpoint: **`/replicas`**

#### GET /replicas
Retorna um documento JSON com o endpoint de cada réplica, além de seu identificador único.

* **Código  de resposta de sucesso:**`200 OK`

* **Corpo da resposta:**

  ```json
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

#### POST /replicas
Recebe um documento JSON com o endpoint de cada réplica, além de seu identificador único.
* **Código  de resposta de sucesso:**`201 CREATED`

* **Corpo da requisição:**

  ```json
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


* **Corpo da resposta:**

  ```json{
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
  
#### DELETE /replicas
Delete a lista de replicas do servidor.
* **Código  de resposta de sucesso:**`200 OK`

## Transações

Endpoint: **`/transaction`**

#### PUT /transaction
Receber um documento JSON com a ação que deverá ser enviadapara todas as réplicas. A ação poderá ser um saque (débito) ou depósito (crédito) de umaquantia em uma determinada conta. Toda ação deverá ter um identificador único.
* **Código  de resposta de sucesso:**`201 OK`
* **Código  de resposta de falha:**`403 Forbidden`

* **Corpo da requisição:**

  ```json{
  {
  "id" : "11111-LLLCCC-dsad-b2b6-dasd",
  "operation" : "debito",
  "account" : 1,
  "value" : 10
  }

#### GET /transaction
Retorna um documento JSON com a lista de ações que foram processadas. Esse documento deverá conter o identificador único de cada transação e a situação da mesma:success se ela foi processada ou fail, caso contrário.
* **Código  de resposta de sucesso:**`200 OK`

* **Corpo da resposta:**
  ```json{
    {
      "actions": [
        {
          "id": "313nm23n331",
          "status": "success"
        },
        {
          "id": "332131dada1211",
          "status": "success"
        },
        {
          "id": "19148f6d-1318-4887-b2b6-215bfc8ac35f",
          "status": "success"
        },
        {
          "id": "19148f6d-1318-4887-b2b6-dasd",
          "status": "success"
        },
        {
          "id": "asdasdsa-asdasd-dsad-b2b6-dasd",
          "status": "success"
        },
        {
          "id": "dasda333-asdasd-dsad-b2b6-dasd",
          "status": "success"
        },
        {
          "id": "11111-asdasd-dsad-b2b6-dasd",
          "status": "success"
        },
        {
          "id": "11111-asdas222d-dsad-b2b6-dasd",
          "status": "success"
        },
        {
          "id": "11111-asdas2223333d-dsad-b2b6-dasd",
          "status": "success"
        },
        {
          "id": "11111-asdas2223333333339d-dsad-b2b6-dasd",
          "status": "success"
        },
        {
          "id": "11111-LLL-dsad-b2b6-dasd",
          "status": "success"
        },
        {
          "id": "11111-LLLCCC-dsad-b2b6-dasd",
          "status": "fail"
        }
      ]
    }

## Semente

Endpoint: **`/seed`**

#### POST /seed
Recebe um  número  inteiro  em  um  documento  JSON  que deverá ser usado como semente do gerador de números pseudo aleatórios, que é usadoquando o processo for uma réplica durante a fase de votação.
* **Código  de resposta de sucesso:**`200 OK`
* **Corpo da requisição:**
```json{
  {"seed":12345}



