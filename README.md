# Processo seletivo Resh Cyber Defense

# Como rodar o projeto

# No terminal:

-Criar os Serviços do postgresql e python com o docker.

```
docker-compose up --build
```

-Subir o Servidor com o docker.

```
docker-compose up -d
```

- Para rodar os testes:
```
docker-compose exec resh pytest
```