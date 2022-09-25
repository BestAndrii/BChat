"""Сервер чата."""


import socket
import threading


# Класс сервера
class Server:
    """Класс для сервера чата."""

    def __init__(self, ip: str, port: int):
        # Создаём сокет сервера
        self.server = socket.socket()
        self.server.bind((ip, port))

        self.server.listen(0)
        self.all_clients: list = []

        print("Сервер запущен!")

        self.new_user()

    # Подключение новых пользователей
    def new_user(self):
        while True:
            user, adress = self.server.accept()
            print("connect")

            name = user.recv(1024).decode("utf-32")

            # Если клиента нету в списке self.all_clients
            if user != self.all_clients:
                self.all_clients.append(user)
                user.send("Успешное подключение к чату!".encode("utf-32"))

                # Отправляем всем клиентом сообщение о подключении
                for client in self.all_clients:
                    if client != user:
                        client.send(f"{name} подключился/подключилась к чату!".encode("utf-32"))

                # Запускаем поток для обработки сообщений клиента
                threading.Thread(
                    target=self.monitor_user,
                    args=(name, user,)
                ).start()

    # Мониторинг сообщений пользователя
    def monitor_user(self, nik: str, client_socket: socket.socket):
        while True:
            data = client_socket.recv(1024)

            # Удаление сокета клиента из списка
            if data == b"exit":
                self.all_clients.remove(client_socket)

                # Отправляем сообщение об отключении
                for client in self.all_clients:
                    client.send(f"{nik} отключился/отключилась от чата!".encode("utf-32"))

                break

            # Отправка сообщения клиента всем пользователям
            for client in self.all_clients:
                if client != client_socket:
                    message = data.decode("utf-32")
                    client.send(f"{nik}: {message}".encode("utf-32"))


if __name__ == "__main__":
    myserver: Server = Server("127.0.0.1", 54321)
