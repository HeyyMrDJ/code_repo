'Socket server'
import socketserver

NAME = 'Localhost'
PORT = 5010


class SocketHandler(socketserver.BaseRequestHandler):
    'Socket Handler'
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} wrote:")
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    with socketserver.TCPServer((NAME, PORT), SocketHandler) as server:
        server.serve_forever()
