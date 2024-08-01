import socket
import threading

class LoadBalancer:
    def __init__(self, host, port, servers):
        self.host = host
        self.port = port
        self.servers = servers
        self.server_index = 0
        self.lock = threading.Lock()

    def get_next_server(self):
        with self.lock:
            server = self.servers[self.server_index]
            self.server_index = (self.server_index + 1) % len(self.servers)
        return server

    def handle_client(self, client_socket):
        server = self.get_next_server()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect(server)
        
        threading.Thread(target=self.forward, args=(client_socket, server_socket)).start()
        threading.Thread(target=self.forward, args=(server_socket, client_socket)).start()

    def forward(self, source, destination):
        while True:
            data = source.recv(4096)
            if not data:
                break
            destination.send(data)
        source.close()
        destination.close()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Load balancer started on {self.host}:{self.port}")

        while True:
            client_socket, _ = server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket)).start()

if __name__ == "__main__":
    servers = [("127.0.0.1", 8001), ("127.0.0.1", 8002)]
    load_balancer = LoadBalancer("0.0.0.0", 8000, servers)
    load_balancer.start()