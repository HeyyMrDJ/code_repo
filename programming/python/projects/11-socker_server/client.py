'Socket cliet'
import socket

SERVER_NAME = 'Localhost'
SERVER_PORT = 5010
USER_NAME = 'DJ'


def client_connection(server_name, server_port):
    'Function to open connection to server'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        client_input = input('--> ')
        sock.connect((server_name, server_port))
        sock.sendall(bytes(client_input + "\n", "utf-8"))
        client_received = str(sock.recv(1024), "utf-8")
        print(f"{USER_NAME}:     {client_input}")
        print(f"Received: {client_received}")
        sock.close()


while True:
    client_connection(SERVER_NAME, SERVER_PORT)
