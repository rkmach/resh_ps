# Processo seletivo Resh Cyber Defense

# Como rodar o projeto

# No terminal:

- Criar um ambiente virtual e instalar os requirements:

```
pip3 install -r requirements.txt
```

- Fazer as migrações necessárias para criar o bd:

```
python manage.py migrate
```

- Subir o Servidor:

```
python manage.py runserver
```

# No browser

- Acessar o localhost na página de login:
```
http://localhost:8000/pages/login/
```

- Criar um usuário e testar os serviços disponíveis no site.


# Em outro terminal(também com ambiente virtual ativado):

- Testar a API para criar um usuário, os métodos POST e PUT são suportados. Depois é possível ver o novo usuário no banco de dados, ou fazer login no browser ou com a API.

```
curl -d '{"username":"JoaoPedro", "email":"joao@email.com", "phone":"545646", "first_name":"Joao", "last_name":"Pedro", "password":"joao1234", "password2":"joao1234"}' -H "Content-Type: application/json" -X POST http://localhost:8000/pages/registration/
```

```
curl -d '{"username":"Raphael", "email":"raphael@email.com", "phone":"32659874", "first_name":"Raphael", "last_name":"Kaviak", "password":"raphael1234", "password2":"raphael1234"}' -H "Content-Type: application/json" -X PUT http://localhost:8000/pages/registration/
```

- Fazer login. Pode-se usar o email ou nome de usuário(se algum dado estiver errado, não aparecerá o campo 'Set-Cookie' como retorno)

```
curl -i -d '{"username":"JoaoPedro", "password":"joao1234"}' -H "Content-Type: application/json" -X POST http://localhost:8000/pages/login/
```
```
curl -i -d '{"username":"joao@email.com", "password":"joao1234"}' -H "Content-Type: application/json" -X POST http://localhost:8000/pages/login/
```

- A partir daqui as ações devem ser feitas por usuário autenticados. A melhor maneira de informar a autenticação pela API é com um token de autenticação. O token pode ser gerado assim:

```
python manage.py createsuperuser --username Teste --email teste@example.com
```

- Será necessária uma senha, coloque 'resh1234'. Agora podemos gerar o token:

```
python manage.py drf_create_token Teste
```

- Será fornecido um token, que a partir de agora será usado para fazer as requisições e confirmar a autenticação.

- Testando a API de mudar senha usando o método POST(retornará um HTML dizendo que a senha foi alterado com sucesso):

```
curl -d '{"old_password":"resh1234", "new_password":"resh5678"}' -H "Content-Type: application/json" -H "Authorization: Token token_gerado" -X POST  http://localhost:8000/pages/change_password/
```

- Também funciona com o método PUT: 

```
curl -d '{"old_password":"resh5678", "new_password":"resh1234"}' -H "Content-Type: application/json" -H "Authorization: Token token_gerado" -X PUT  http://localhost:8000/pages/change_password/
```


- Testando a API de mudar dados do usuário(não são permitidos campos em branco!):

```
curl -d '{"username":"Resh", "email":"resh@email.com", "phone":"995725731", "first_name":"Resh", "last_name":"Cyber"}' -H "Content-Type: application/json" -H "Authorization: Token token_gerado" -X POST http://localhost:8000/pages/change_info/
```

- Com o método PUT

```
curl -d '{"username":"Resh", "email":"resh@email.com", "phone":"995725731", "first_name":"Resh", "last_name":"Cyber"}' -H "Content-Type: application/json" -H "Authorization: Token token_gerado" -X PUT http://localhost:8000/pages/change_info/
```

- Agora é uma boa hora de voltar ao navegador, fazer login com os novos campos e ver os dados atualizados.

- Finalmente testando a API para excluir o registro

```
curl -H "Authorization: Token token_gerado" -X DELETE http://localhost:8000/pages/delete_account/
```

# Explicações sobre os códigos de backend e frontend.

- As página vistas no navegador são todas processadas no arquivo /pages/view.py. As funções ali definidas suportam os verbos GET(renderizar página com os campos definidos no serializer de cada página), POST(serialização e validação dos dados vindos do formulário HTML por meio de serializers, para que possam ser salvos do banco de dados) e PUT(serialização e validação dos dados vindos como chamadas de API também por meio de serializers, para que possam ser salvos do banco de dados). A página de excluir registro suporta o verbo DELETE.

- Também existe a página http://localhost:8000/users/all_users/, que mostra todos os usuários cadastrados. Ela é consumida pela página de registro de usuário, que faz uma requisição para checar se o nome de usuário ou email já estão em uso, se sim, exibe uma mensagem na tela.

- O HTML das páginas vistas no navegador estão em /templates. Todos os templates extendem o arquivo 'base.html', que contém o esqueleto principal do site(navbar, footer, incluir arquivos estáticos).

- O modelo de usuário usado extende o modelo padrão do django (django.contrib.auth.models.AbstractUser), adicionando o campo 'phone'.

- No diretório /static estão os arquivos considerados estáticos(imagens, css, javascript)

- Na páginas de registro de usuário e alteração de dados, há um validação feita em javascript (usando a API citada acima que lista todos os campos) que mostra se existem usernames ou emails iguais a este que você quer cadastrar/alterar, além de alertar se as senhas casam ou não.

- Apps criados por mim são somente users e pages, também são usados os apps do rest_framework padrão e para gerar tokens. O app fontawesome-free é usado para estilizar o frontend com ícones.

- Como formulários HTML suportam apenas os métodos GET e POST, esses são os métodos são usados quando a requisição é feita pelo browser, quando feita pelo curl, pode-se usar o verbo PUT e DELETE. Também por essa razão algumas requisições feitas com POST pelo curl não geram mensagens de confirmação como aquelas feitas com PUT. 

- Não é possível criar usuários com o mesmo email ou com o mesmo username, se acontecer uma requisição deste tipo ela será descartada.

- Na página de alteração de dados, as informações do usuário só serão trocadas se todos os campos forem preenchidos corretamente e não houver usernames ou email repetidos.





