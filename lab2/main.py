import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

from lab2.data.InMemoryWordsProvider import InMemoryWordsProvider
from lab2.phase.templates.factory.GangstaTemplateFactory import GangstaTemplateFactory
from lab2.phase.templates.factory.PhilosophicalTemplateFactory import RomanticTemplateFactory
from lab2.phase.templates.factory.RomanticTemplateFactory import PhilosophicalTemplateFactory


class QuoteGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор Цитат")
        self.setStyleSheet("background-color: #2E2E2E; color: white;")

        self.words_provider = InMemoryWordsProvider()
        self.gangsta_factory = GangstaTemplateFactory()
        self.romantic_factory = RomanticTemplateFactory()
        self.philosophical_factory = PhilosophicalTemplateFactory()

        self.quote_label = QLabel("Нажмите кнопку, чтобы сгенерировать цитату!")
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setStyleSheet("font-size: 24px; font-style: italic;")

        self.gangsta_button = QPushButton("Гангста Цитата")
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
        word_set = self.words_provider.generate_word_set()
        quote = self.gangsta_factory.create_template()(word_set)
        self.quote_label.setText(quote)

    def generate_romantic_quote(self):
        word_set = self.words_provider.generate_word_set()
        quote = self.romantic_factory.create_template()(word_set)
        self.quote_label.setText(quote)

    def generate_philosophical_quote(self):
        word_set = self.words_provider.generate_word_set()
        quote = self.philosophical_factory.create_template()(word_set)
        self.quote_label.setText(quote)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuoteGeneratorApp()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
