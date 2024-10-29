import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, \
    QMessageBox
from tasks.first import generate_random_notes
from tasks.second import multiples_of_three
from tasks.third import filter_valid_emails


class GeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генераторы и проверка email")

        self.tabs = QTabWidget()

        self.tab_random_notes()
        self.tab_multiples_of_three()
        self.tab_email_filter()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def tab_random_notes(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.notes_output = QTextEdit()
        self.notes_output.setReadOnly(True)

        generate_button = QPushButton("Сгенерировать первые 20 случайных нот")
        generate_button.clicked.connect(self.display_random_notes)

        layout.addWidget(QLabel("Генерация случайных нот:"))
        layout.addWidget(generate_button)
        layout.addWidget(self.notes_output)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "Случайные ноты")

    def display_random_notes(self):
        try:
            random_notes = generate_random_notes()  # Используем функцию из tasks.first
            self.notes_output.setText(", ".join(random_notes))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка генерации", f"Произошла ошибка: {e}")

    def tab_multiples_of_three(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.start_input = QLineEdit()
        self.start_input.setPlaceholderText("Введите начальное значение a")

        self.multiples_output = QTextEdit()
        self.multiples_output.setReadOnly(True)

        generate_button = QPushButton("Сгенерировать первые 20 чисел, кратных 3")
        generate_button.clicked.connect(self.display_multiples_of_three)

        layout.addWidget(QLabel("Генерация чисел, кратных 3:"))
        layout.addWidget(self.start_input)
        layout.addWidget(generate_button)
        layout.addWidget(self.multiples_output)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "Числа, кратные 3")

    def display_multiples_of_three(self):
        try:
            a = int(self.start_input.text())
            generator = multiples_of_three(a)
            multiples = [next(generator) for _ in range(20)]
            self.multiples_output.setText(", ".join(map(str, multiples)))
        except ValueError:
            QMessageBox.critical(self, "Ошибка ввода", "Введите целое число.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка генерации", f"Произошла ошибка: {e}")

    def tab_email_filter(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Введите email-адреса через пробел")

        self.email_output = QTextEdit()
        self.email_output.setReadOnly(True)

        filter_button = QPushButton("Отфильтровать корректные email")
        filter_button.clicked.connect(self.display_filtered_emails)

        layout.addWidget(QLabel("Фильтрация email-адресов:"))
        layout.addWidget(self.email_input)
        layout.addWidget(filter_button)
        layout.addWidget(self.email_output)

        tab.setLayout(layout)
        self.tabs.addTab(tab, "Фильтрация email")

    def display_filtered_emails(self):
        try:
            emails = self.email_input.text()
            valid_emails = filter_valid_emails(emails)
            self.email_output.setText("\n".join(valid_emails) if valid_emails else "Нет корректных email-адресов.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка фильтрации", f"Произошла ошибка: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeneratorApp()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
