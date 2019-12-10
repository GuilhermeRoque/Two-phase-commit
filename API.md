# Documentação da API do Web Service

> O documento descreve API REST do Serviço Web fornecido pela solução Home Tasks. 

***

**OBS.:** Todas as requisições efetuadas, com exceção do Registro, necessitam que o usuário esteja previamente autenticado. Por isso o envio de um Token, retornado do processo de autenticação, no cabeçalho é `OBRIGATÓRIO`. `token: "token"`

***

Os seguintes erros podem ser retornados em qualquer requisição, que necessite de autenticação, caso o Usuário não informe o token ou não tenha permissão.

**Código de resposta de erro:**`401 UNAUTHORIZED`

Quando é feita a requisição sem informar o token ou o mesmo não é válido.

**Corpo da resposta:**

```json
{
	"error": "Autenticação Necessária"
}
```

**Código de resposta de erro:**`403 FORBIDDEN`

Caso o usuário autenticado tenha um token válido, mas não tenha permissão para efetuar a requisição.

**Corpo da resposta:**

```json
{
	"error": "Permissão Negada"
}
```


**URL Base:** `/hometasks/api/v1/`



## Autenticação

Endpoint: **`/login`**


#### POST /login

Realiza a autenticação do usuário junto ao servidor. Necessário o envio das credenciais do usuário no cabeçalho da requisição. Retorna o token de autenticação caso a autenticação tenha ocorrido com sucesso.

* **Requisitos:** 

  Cabeçalho `Authorization: Basic <idUsuario:senha>`, com `idUsuario:senha` codificados em Base 64, na requisição.

* **Código  de resposta de sucesso:**`200 OK`

  Autenticação realizada com sucesso.

* **Corpo da resposta:**

  ```json
  {
      "token": "7ba40d1a6034ac67a2805bfca21cbbf723d0311b"
  }
  ```

* **Código de resposta de erro:**`400 BAD REQUEST`

  1. Credenciais não enviadas no cabeçalho Authorization da Requisição.
  * **Corpo da resposta:**

    ```json
  {
        "error": "Credenciais não enviadas no cabeçalho Authorization"
  }
    ```
  2. Formato de envio das credenciais não foi reconhecido.
  * **Corpo da resposta:**

    ```json
  {
        "error": "Formato das credenciais inválido. Correto - Base64(idUsuario:senha)"
  }
    ```
* **Código de resposta de erro:**`404 NOT FOUND`

	Usuário não encontrado.

* **Corpo da resposta:**

  ```json
  {
        "error": "idUsuario inválido ou inexistente"
  }
  ```
  
* **Código de resposta de erro:**`401 UNAUTHORIZED`
  
	Senha inválida.
  
* **Corpo da resposta:**
  
  ```json
  {
        "error": "senha inválida"
  }
  ```





***



## Lista de endpoints e métodos


1. [Usuário.](./subDoc/users.md)
2. [Tarefa.](./subDoc/tasks.md)
3. [Comentário.](./subDoc/comments.md)
4. [Rotina.](./subDoc/routines.md)
5. [Casa.](./subDoc/home.md)
6. [Conta.](./subDoc/account.md)
7. [Regra.](./subDoc/rules.md)
