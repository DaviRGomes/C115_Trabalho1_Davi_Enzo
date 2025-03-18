
# Server\_Client

Este projeto implementa uma comunicação entre um servidor e um cliente utilizando sockets em Python. O servidor envia perguntas para o cliente, recebe as respostas e avalia o desempenho do usuário.

## Estrutura do Projeto

```bash
Server_Client/
│── server/
│   ├── server.py
│   ├── questions.json
│
│── client/
│   ├── client.py
```

## Como Executar

### 1. Clone o projeto

```bash
git clone https://github.com/DaviRGomes/C115_Trabalho1_Davi_Enzo
```

### 2. Entre no diretório do projeto

```bash
cd C115_Trabalho1_Davi_Enzo
```

### 3. Iniciar o Servidor

Abra um terminal e execute os seguintes comandos:

```bash
cd server
python server.py
```

O servidor ficará aguardando conexões de clientes.

### 4. Iniciar o Cliente

Em outro terminal, execute:

```bash
cd client
python client.py
```

O cliente receberá as perguntas do servidor e permitirá ao usuário responder.

## Funcionamento

1. O servidor carrega um arquivo `questions.json` contendo as perguntas e alternativas.
2. O servidor envia as perguntas para o cliente.
3. O cliente recebe e exibe cada pergunta e envia as respostas ao servidor.
4. O servidor avalia as respostas e retorna o resultado final.

## Exemplo de Formato do `questions.json`

```json
[
    {
    "question": "Qual é a capital do Brasil?",
    "options": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
    "correct_answer": "Brasília"
    }
]
```

## Autor

Projeto desenvolvido por Davi Rosa Gomes e Enzo Augusto do Couto

