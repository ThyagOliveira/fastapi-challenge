# Desafio Python

O desafio consiste em construir uma api de localização que leia um JSON contendo posições GPS seguindo os seguintes critérios:

- Armazenar os dados nas tabelas no banco de dados, uma contendo o identificador do device, outra contendo as posições de localização.

- Construir uma rota GET que restaure as informações podendo filtrar por device.

- Utilizar como framework de desenvolvimento FastAPI e o banco de dados da sua escolha (pode ser DB SQLite).

- Desejável, mas não obrigatório, adicionar Docker ou devcontainer do VSCODE.

Estrutura JSON a ser lida:
```
[
    {
        device_id: 5555,
        latitude: -30.156180,
        longitude: -51.197909
    },
    {
        device_id: 5555,
        latitude: -30.178911,
        longitude: -51.197909
    },
    {
        device_id: 5555,
        latitude: -30.197632,
        longitude: -51.197909
    }
]
```

## Instruções Gerais

Para configurar o ambiente crie um arquivo .env conforme o exemplo em [.env.example](.env.example) e em seguida execute os seguintes comandos

```
$ docker-compose build
$ docker-compose up
```

Para acessar a documentação da API

```
http://0.0.0.0:8000/docs
```


