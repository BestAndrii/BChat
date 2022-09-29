"""Онлайн чат на Python.

Для запуска нужно:
    - pip install pyqt5.
"""


import sys
import threading

from socket import socket
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from des import Ui_MainWindow


# Класс создаёт окно программы
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загружаем дизайн
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Обработчики кнопок
        self.ui.pushButton_3.clicked.connect(self.connect_to_server)
        self.ui.pushButton_2.clicked.connect(self.clear_panel_text)
        self.ui.pushButton.clicked.connect(self.send_message)

        # Блокируем кнопки чата
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.setEnabled(False)

    # Очистка панели пользователя
    def clear_panel_text(self):
        self.ui.textBrowser.clear()
        self.ui.textBrowser_2.clear()

    # Получение сообщений от сервера
    def get_message(self, client_socket: socket):
        while True:
            data = client_socket.recv(1024)
            decode_data = data.decode("utf-32")

            if decode_data:
                print(data)
                self.ui.textBrowser.append(decode_data)
                self.ui.textBrowser_2.append(decode_data)

    # Есть ли текст в панели или нет
    def panel_text(self):
        while True:
            # Текста из панелей
            text1 = self.ui.textBrowser.toPlainText()
            text2 = self.ui.textBrowser_2.toPlainText()

            if text1 and text2:
                self.ui.pushButton_2.setEnabled(True)

            else:
                self.ui.pushButton_2.setEnabled(False)

    # Пустое сообщение или нет
    def message_text(self):
        while True:
            message = self.ui.lineEdit.text()

            if message:
                self.ui.pushButton.setEnabled(True)

            else:
                self.ui.pushButton.setEnabled(False)

    # Отправить сообщение
    def send_message(self):
        message = self.ui.lineEdit.text()

        if message:
            self.client.send(message.encode("utf-32"))

            message = f"{self.name} [Вы]: {message}"

            # Выводим наше сообщение в панели
            self.ui.textBrowser.append(message)
            self.ui.textBrowser_2.append(message)

    # Подключение к серверу
    def connect_to_server(self):
        ip = self.ui.lineEdit_2.text()
        port = self.ui.lineEdit_3.text()
        self.name = self.ui.lineEdit_4.text()

        try:
            # Если IP не пустой
            if ip:
                # Если порт не пустой
                if port:
                    # Если имя не пустое
                    if self.name:
                        self.client = socket()
                        self.client.connect((ip, int(port)))

                        self.client.send(self.name.encode("utf-32"))

                        # Запускаем поток для получения сообщений от сервера
                        threading.Thread(
                            target=self.get_message,
                            args=(self.client,)).start()

                        threading.Thread(
                            target=self.panel_text).start()

                        threading.Thread(
                            target=self.message_text).start()

                        # Разблокируем кнопку очистить
                        self.ui.pushButton_2.setEnabled(True)

                        # Блокируем кнопку подключения
                        self.ui.pushButton_3.setEnabled(False)

                    # Если имя пустое
                    else:
                        port_warning = QMessageBox()
                        port_warning.setText("Вы не ввели имя")
                        port_warning.exec_()

                # Если порт пустой
                else:
                    port_warning = QMessageBox()
                    port_warning.setText("Вы не ввели порт")
                    port_warning.exec_()

            # Если IP пустой
            else:
                ip_warning = QMessageBox()
                ip_warning.setText("Вы не ввели IP")
                ip_warning.exec_()

        except (ValueError, ConnectionError, ConnectionResetError):
            ip_warning = QMessageBox()
            ip_warning.setText("Проверьте правильность ввода данных!")
            ip_warning.exec_()

    # Событие при завершении программы
    def closeEvent(self, _):
        try:
            self.client.send(b"exit")

        except (AttributeError, ConnectionError, ConnectionResetError):
            pass


# Функция запускает программу
def start_app():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_app()
