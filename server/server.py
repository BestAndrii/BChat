import socket
import threading


class Server:
    def __init__(self, ip: str, port: int):
        self.server: socket.socket = socket.socket()
        self.server.bind((ip, port))

        self.all_clients: list = []
        self.server.listen(0)

        print("Сервер запущен!")

        self.new_user()

    def new_user(self):
        while True:
            user, adress = self.server.accept()

            for i in self.all_clients:
                if i != user:
                    i.send("Новый пользователь подключился к чату!".encode())

            if user not in self.all_clients:
                self.all_clients.append(user)
                user.send("Успешное подключение к серверу!".encode())

                threading.Thread(
                    target=self.message_handler,
                    args=(user,)).start()

    def message_handler(self, client_socket: socket.socket):
        while True:
            data = client_socket.recv(1024)

            # --
            if data.decode():
                print(data)
            # --

            if data == b"exit":
                self.all_clients.remove(client_socket)

                for i in self.all_clients:
                    if i != client_socket:
                        i.send("Пользователь ушел с чата!".encode())

                break

            for i in self.all_clients:
                if i != client_socket:
                    i.send(data)


if __name__ == "__main__":
    myserver = Server(ip="127.0.0.1", port=5000)
