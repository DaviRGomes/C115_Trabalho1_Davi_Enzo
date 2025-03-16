import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        # Recebe a pergunta do servidor
        question = client_socket.recv(1024).decode()
        if not question:  # Se não houver mais perguntas, encerra
            break

        print(question)
        response = input("Sua resposta: ")
        client_socket.send(response.encode())  # Envia a resposta ao servidor

    # Cliente recebe o resultado final
    result = client_socket.recv(1024).decode()
    print(result)

    client_socket.close()

if __name__ == "__main__":
    start_client()