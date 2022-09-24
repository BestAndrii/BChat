import socket
import sys
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from des import Interface


# Класс для дизайна клиента
class Client(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загружаем дизайн из des.py
        self.ui = Interface()
        self.ui.setupUi(self)

        # Блокируем чат
        self.ui.Send.setEnabled(False)
        self.ui.Connect.setEnabled(False)
        self.ui.Message.setEnabled(False)

        self.ui.pushButton.clicked.connect(self.save_settings)
        self.ui.Connect.clicked.connect(self.connect_to_server)
        self.ui.Send.clicked.connect(self.send_message)

    def save_settings(self):
        if self.ui.lineEdit.text() == "" and self.ui.lineEdit_2.text() == "":
            warning = QMessageBox()
            warning.setText("Вы не указали данные")
            warning.exec_()

        else:
            if self.ui.lineEdit.text() == "":
                warning = QMessageBox()
                warning.setText("Вы не указали IP")
                warning.exec_()

            else:
                self.ip: str = self.ui.lineEdit.text()

                if self.ui.lineEdit_2.text() == "":
                    warning = QMessageBox()
                    warning.setText("Вы не указали порт")
                    warning.exec_()

                else:
                    try:
                        if int(self.ui.lineEdit_2.text()) < 1:
                            warning = QMessageBox()
                            warning.setText("Порт должен быть выше одного")
                            warning.exec_()

                        else:
                            self.port: int = int(self.ui.lineEdit_2.text())

                            self.ui.Connect.setEnabled(True)

                    except ValueError:
                        value_error = QMessageBox()
                        value_error.setText("Порт должен содержать только цифры!")
                        value_error.exec_()

    def send_message(self):
        message = self.ui.Message.text()

        if message:
            self.client.send(message.encode())
            self.ui.Information.append(f"[Вы]: {message}")

        else:
            warning = QMessageBox()
            warning.setText("Вы не можете отправить пустое сообщение")
            warning.exec_()

    def message_monitor(self, client_socket: socket.socket):
        while True:
            try:
                self.data = client_socket.recv(1024).decode()

                if self.data:
                    self.ui.Information.append(self.data)

            except ConnectionResetError:
                error = QMessageBox()
                error.setText("Сервер разорвал соединение!")
                error.exec_()

    def connect_to_server(self):
        try:
            self.client = socket.socket()
            self.client.connect((self.ip, self.port))

            threading.Thread(target=self.message_monitor,
                             args=(self.client,)).start()

            self.ui.Connect.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
            self.ui.Send.setEnabled(True)
            self.ui.Message.setEnabled(True)
            self.ui.lineEdit.setEnabled(False)
            self.ui.lineEdit_2.setEnabled(False)

        except (ConnectionRefusedError, socket.gaierror):
            connection_error = QMessageBox()
            connection_error.setText("Не удалось подключиться к серверу")
            connection_error.exec_()

            self.ui.Connect.setEnabled(False)

    def closeEvent(self, event):
        try:
            self.client.send(b"exit")

        except AttributeError:
            pass


# Запуск приложения
def start():
    app = QApplication(sys.argv)
    window = Client()
    window.show()
    sys.exit(app.exec_())
