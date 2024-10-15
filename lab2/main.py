import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtGui import QPainter, QPixmap
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
        self.background = QPixmap('server/resources/static/volk.png')

        self.quote_label = QLabel("Нажмите кнопку, чтобы сгенерировать цитату!")
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setStyleSheet("""
            font-size: 40px;
            font-style: italic;
            font-family: 'Haettenschweiler';
            color: white;
            margin-top: 300px;
        """)
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

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

    def paintEvent(self, event):
        painter = QPainter(self)
        window_rect = self.rect()
        background_rect = window_rect.adjusted(0, 0, 0, -window_rect.height() // 2)
        painter.drawPixmap(background_rect, self.background)
        painter.fillRect(0, self.height() // 2, self.width(), self.height() // 2, Qt.black)


    def generate_gangsta_quote(self):
        self.play_sound()
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

    def play_sound(self):
        file = QUrl.fromLocalFile("server/resources/static/bezumno.mp3")
        self.player.setSource(file)
        self.player.play()

if __name__ == "__main__":
    # TODO readme и рекуаирменты додедалть
    # TODO свои эксепшены
    app = QApplication(sys.argv)
    window = QuoteGeneratorApp()
    window.resize(500, 600)
    window.show()
    sys.exit(app.exec())
