import socket
import json
import os


def load_questions():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'questions.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    return questions

def start_server():
    questions = load_questions()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Servidor aguardando conexões...")

    client_socket, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")

    responses = []
    for q in questions:
        # Envia a pergunta atual
        question_str = f"{q['question']}\n" + "\n".join(q['options']) + "\n"
        client_socket.send(question_str.encode())

        # Aguarda a resposta do cliente
        response = client_socket.recv(1024).decode().strip()
        responses.append(response)

    # Verifica as respostas e envia o resultado
    results = []
    correct_count = 0
    for i, response in enumerate(responses):
        if response == questions[i]['correct_answer']:
            correct_count += 1
            results.append(f"Questão {i+1}: Acerto (Acertos: {correct_count})")
        else:
            results.append(f"Questão {i+1}: Erro")

    # Servidor envia o resultado final
    result_str = f"Você acertou {correct_count} de {len(questions)} questões.\n" + "\n".join(results)
    client_socket.send(result_str.encode())  # Envia o resultado final

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()