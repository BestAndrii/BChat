"""Сервер."""


from threading import Thread
from socket import socket


# Класс сервера
class Server:
    def __init__(self, ip, port):
        # Создаём сокет сервера
        self.server = socket()
        self.server.bind((ip, port))

        self.server.listen(0)
        self.all_clients = []  # Список всех клиентов

        self.new_user()

    # Отправка сообщения всем пользовалелям
    def send_message(self, client_socket, message):
        for client in self.all_clients:
            if client != client_socket:
                client.send(message.encode("utf-32"))

    # Принимает новых пользователей
    def new_user(self):
        while True:
            user, adress = self.server.accept()
            nik = user.recv(1024).decode("utf-32")
            print("connect")

            if user not in self.all_clients:
                self.all_clients.append(user)

                user.send("Успешное покдлючение к чату!".encode("utf-32"))

                # Отправляем сообщение о подключении
                self.send_message(user, f"{nik} подключился к чату!")

                Thread(
                    target=self.message_handler,
                    args=(nik, user,)).start()

    # Обработка сообщений пользователя
    def message_handler(self, nik, client_socket: socket):
        while True:
            data = client_socket.recv(1024)

            if data == b"exit":
                self.all_clients.remove(client_socket)

                self.send_message(client_socket, f"{nik} покинул чат!")
                break

            self.send_message(client_socket, f"{nik}: {data}")


if __name__ == "__main__":
    Server("127.0.0.1", 9879)
