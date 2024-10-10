import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog, QMessageBox
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

def add_word(add_url, word_type):
    word, ok = QInputDialog.getText(None, f"Добавить {word_type}", f"Введите {word_type}:")
    if ok and word:
        try:
            response = requests.post(add_url, json={"word": word})
            response.raise_for_status()
            return f"{word_type.capitalize()} '{word}' добавлено успешно!"
        except requests.exceptions.RequestException as e:
            return f"Ошибка при добавлении {word_type}."
    return f"{word_type.capitalize()} не добавлено."

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

        self.add_noun_button = QPushButton("Добавить Существительное")
        self.add_noun_button.clicked.connect(self.add_noun)

        self.add_verb_button = QPushButton("Добавить Глагол")
        self.add_verb_button.clicked.connect(self.add_verb)

        self.add_adjective_button = QPushButton("Добавить Прилагательное")
        self.add_adjective_button.clicked.connect(self.add_adjective)

        self.exit_button = QPushButton("Выход")
        self.exit_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.quote_label)
        layout.addWidget(self.gangsta_button)
        layout.addWidget(self.romantic_button)
        layout.addWidget(self.philosophical_button)
        layout.addWidget(self.add_noun_button)
        layout.addWidget(self.add_verb_button)
        layout.addWidget(self.add_adjective_button)
        layout.addWidget(self.exit_button)

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

    def add_noun(self):
        result = add_word(url + "/add/noun", "существительное")
        QMessageBox.information(self, "Результат", result)

    def add_verb(self):
        result = add_word(url + "/add/verb", "глагол")
        QMessageBox.information(self, "Результат", result)

    def add_adjective(self):
        result = add_word(url + "/add/adjective", "прилагательное")
        QMessageBox.information(self, "Результат", result)

if __name__ == "__main__":
    # TODO pytest
    # TODO docker server
    # TODO readme
    # TODO свои эксепшены
    # TODO веб интерфейс доделать
    app = QApplication(sys.argv)
    window = QuoteGeneratorApp()
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec())
