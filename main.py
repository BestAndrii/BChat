"""Чат на Python PyQt5."""


import sys
import socket
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from des import UiMainWindow


# Окно программы
class MainWindow(QMainWindow):
    """Класс создаёт главное окно программы."""

    def __init__(self):
        super().__init__()

        # Загружаем дизайн
        self.ui = UiMainWindow()
        self.ui.setupUi(self)

        # Блокируем чат
        self.ui.pushButton.setEnabled(False)
        self.ui.lineEdit.setEnabled(False)

        self.ui.pushButton_2.clicked.connect(self.connect_to_server)
        self.ui.pushButton.clicked.connect(self.send_message)

    # Отправка сообщения
    def send_message(self):
        message = self.ui.lineEdit.text()

        if message:
            self.client.send(message.encode("utf-32"))
            self.ui.textBrowser.append(f"{self.ui.lineEdit_4.text()} [Вы]: {message}")

    # Мониторинг входящих сообщений
    def monitor_messages(self, client_socket: socket.socket):
        while True:
            data = client_socket.recv(1024)

            if data.decode("utf-32"):
                print(data.decode("utf-32"))
                self.ui.textBrowser.append(data.decode("utf-32"))

    # Подключение к серверу
    def connect_to_server(self):
        """Используется для подключения к серверу."""
        try:
            # Если имя не пустое
            if self.ui.lineEdit_4.text():
                self.client = socket.socket()
                self.client.connect((self.ui.lineEdit_2.text(), int(self.ui.lineEdit_3.text())))

                self.client.send(self.ui.lineEdit_4.text().encode("utf-32"))  # Присылаем наше имя серверу
                threading.Thread(
                    target=self.monitor_messages,
                    args=(self.client,)
                ).start()

                # Разблокируем чат
                self.ui.pushButton.setEnabled(True)
                self.ui.lineEdit.setEnabled(True)

            # Если имя пустое
            else:
                error = QMessageBox()
                error.setText("Введите ваше имя!")
                error.exec_()

        except:
            error = QMessageBox()
            error.setText("Проверьте правильность ввода данных!")
            error.exec_()

    # Событие при закрытии программы
    def closeEvent(self, _):
        try:
            self.client.send(b"exit")

        except AttributeError:
            pass


# Запуск чата
def launch_chat():
    """Функция создана для запуска чата.

    Запускает чат.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    launch_chat()
