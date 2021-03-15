# Processo seletivo Resh Cyber Defense

# Como rodar o projeto

# No terminal:

-Criar um ambiente virtual e instalar os requirements:

```
pip install -r requirements.txt
```

-Subir o Servidor:

```
python manage.py runserver
```

# No browser

- Acessar o localhost na página de login:
```
http://localhost:8000/pages/login/
```

- Criar um usuário e testar os serviços disponíveis no site.


# No terminal:

-Testar a API para criar um usuário. Depois é possível ver o novo usuário no banco de dados, ou fazer login no browser ou com a API.

```
curl -d '{"username":"JoaoPedro", "email":"joao@email.com", "phone":"545646", "first_name":"Joao", "last_name":"Pedro", "password":"joao1234", "password2":"joao1234"}' -H "Content-Type: application/json" -X POST http://localhost:8000/pages/registration/
```

-Fazer login. Pode-se usar o email ou nome de usuário.

```
curl -d '{"username":"JoaoPedro", "password":"joao1234"}' -H "Content-Type: application/json" -X POST http://localhost:8000/pages/login/
```
```
curl -d '{"username":"joao@email.com", "password":"joao1234"}' -H "Content-Type: application/json" -X POST http://localhost:8000/pages/login/
```

-A partir daqui as ações devem ser feitas por usuário autenticados. A melhor maneira de informar a autenticação pela API é com um token de autenticação. O token pode ser gerado assim:

```
python manage.py createsuperuser --username Teste --email teste@example.com
```

-Será necessária uma senha, coloque 'resh1234'. Agora podemos gerar o token:

```
python manage.py drf_create_token Teste
```
-Será fornecido um token, que a partir de agora será usado para fazer as requisições e confirmar a autenticação.

-Testando a API de mudar senha:

```
curl -d '{"old_password":"resh1234", "new_password":"resh5678"}' -H "Content-Type: application/json" -H "Authorization: Token token_gerado" -X POST  http://localhost:8000/pages/change_password/
```

-Também funciona com o método PUT: 

```
curl -d '{"old_password":"resh5678", "new_password":"resh1234"}' -H "Content-Type: application/json" -H "Authorization: Token token_gerado" -X PUT  http://localhost:8000/pages/change_password/
```


-Testando a API de mudar dados do usuário:

```
curl -d '{"username":"Resh", "email":"resh@email.com", "phone":"995725731", "first_name":"Resh", "last_name":"Cyber"}' -H "Content-Type: application/json" -H "Authorization: Token token_gerado" -X POST http://localhost:8000/pages/change_info/
```

-Com o método PUT

```
curl -d '{"username":"Bolassa", "email":"boleta@email.com", "phone":"995725731", "first_name":"Bola", "last_name":"Marcos"}' -H "Content-Type: application/json" -H "Authorization: Token 8192e4abdba329b89d6f9e2f77b4cf8b342db42a" -X PUT http://localhost:8000/pages/change_info/
```

-Agora é uma boa hora de voltar ao navegador, fazer login com os novos campos e ver os dados atualizados.

-Finalmente testando a API para excluir o registro

```
curl -H "Authorization: Token token_gerado" -X DELETE http://localhost:8000/pages/delete_account/
```

# No browser

-Na página de registro de usuário, há um validação feita em javascript (que consome uma API que lista todos os campos)que mostra se existem usernames ou emails iguais a este que você quer cadastrar, além de alertar se as senhas casam ou não.