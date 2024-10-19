import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QInputDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtGui import QPainter
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

        # Лейбл для цитат
        self.quote_label = QLabel("Нажмите кнопку, чтобы сгенерировать цитату!")
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setStyleSheet("""
            font-size: 40px;
            font-style: italic;
            font-family: 'Haettenschweiler';
            color: white;
            margin-top: 300px;
        """)

        self.graph_label = QLabel()
        self.graph_label.setAlignment(Qt.AlignCenter)
        self.graph_label.setStyleSheet("background-color: white;")
        self.graph_label.setPixmap(QPixmap())

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

        self.load_graph_button = QPushButton("Показать график активности")
        self.load_graph_button.clicked.connect(self.load_activity_graph)

        self.exit_button = QPushButton("Выход")
        self.exit_button.clicked.connect(self.close)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.graph_label)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.quote_label)
        right_layout.addWidget(self.gangsta_button)
        right_layout.addWidget(self.romantic_button)
        right_layout.addWidget(self.philosophical_button)
        right_layout.addWidget(self.add_noun_button)
        right_layout.addWidget(self.add_verb_button)
        right_layout.addWidget(self.add_adjective_button)
        right_layout.addWidget(self.load_graph_button)
        right_layout.addWidget(self.exit_button)

        main_layout.addLayout(left_layout, 1)  # Левая часть занимает 1/3 ширины
        main_layout.addLayout(right_layout, 2)  # Правая часть занимает 2/3 ширины

        self.setLayout(main_layout)

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

    def load_activity_graph(self):
        # Загружаем график с сервера
        try:
            response = requests.get(url + "/activity-graph", stream=True)
            if response.status_code == 200:
                graph_data = response.content
                pixmap = QPixmap()
                pixmap.loadFromData(graph_data)
                self.graph_label.setPixmap(pixmap.scaled(self.graph_label.size(), Qt.KeepAspectRatio))
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось загрузить график активности.")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Ошибка", "Ошибка при запросе графика активности.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuoteGeneratorApp()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
