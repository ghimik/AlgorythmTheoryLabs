import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
import requests
from server import server

url = 'http://localhost:' + str(server.port)

def fetch_quote(fetch_url):
    try:
        response = requests.get(fetch_url)
        response.raise_for_status()
        quote = response.json().get("quote", "Ошибка получения цитаты.")
        return quote
    except requests.exceptions.RequestException as e:
        return "Ошибка при запросе цитаты."


class QuoteGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор Цитат")
        self.setStyleSheet("background-color: #2E2E2E; color: white;")


        self.quote_label = QLabel("Нажмите кнопку, чтобы сгенерировать цитату!")
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setStyleSheet("font-size: 24px; font-style: italic;")

        self.gangsta_button = QPushButton("Пацанская Цитата")
        self.gangsta_button.clicked.connect(self.generate_gangsta_quote)

        self.romantic_button = QPushButton("Романтическая Цитата")
        self.romantic_button.clicked.connect(self.generate_romantic_quote)

        self.philosophical_button = QPushButton("Философская Цитата")
        self.philosophical_button.clicked.connect(self.generate_philosophical_quote)

        layout = QVBoxLayout()
        layout.addWidget(self.quote_label)
        layout.addWidget(self.gangsta_button)
        layout.addWidget(self.romantic_button)
        layout.addWidget(self.philosophical_button)

        self.setLayout(layout)

    def generate_gangsta_quote(self):
        quote = fetch_quote(url + "/gangsta")
        self.quote_label.setText(quote)

    def generate_romantic_quote(self):
        quote = fetch_quote(url + "/romantic")
        self.quote_label.setText(quote)

    def generate_philosophical_quote(self):
        quote = fetch_quote(url + "/philosophical")
        self.quote_label.setText(quote)


if __name__ == "__main__":
    # TODO pytest
    # TODO ввод новых слов в бд
    # TODO меню и выход
    app = QApplication(sys.argv)
    window = QuoteGeneratorApp()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
