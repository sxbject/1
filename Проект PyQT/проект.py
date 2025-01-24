import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QPlainTextEdit


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Текстовый редактор')

        self.filename_edit = QLineEdit(self)
        self.filename_edit.move(5, 5)
        self.filename_edit.resize(150, 27)

        self.new_button = QPushButton("Создать новый", self)
        self.new_button.move(5, 35)
        self.new_button.resize(150, 27)
        self.new_button.clicked.connect(self.new_btn_func)

        self.save_button = QPushButton("Сохранить файл", self)
        self.save_button.move(5, 65)
        self.save_button.resize(150, 27)
        self.save_button.clicked.connect(self.save_btn_func)

        self.open_button = QPushButton("Открыть файл", self)
        self.open_button.move(5, 95)
        self.open_button.resize(150, 27)
        self.open_button.clicked.connect(self.open_btn_func)

        self.text_edit = QPlainTextEdit(self)
        self.text_edit.move(160, 5)
        self.text_edit.resize(270, 270)

    def new_btn_func(self):
        self.filename_edit.setText("")
        self.text_edit.setPlainText("")

    def save_btn_func(self):
        if self.filename_edit.text() != "":
            with open(self.filename_edit.text(), "w", encoding="utf-8") as file:
                plain_text = self.text_edit.toPlainText()
                file.write(plain_text)

    def open_btn_func(self):
        self.text_edit.clear()
        try:
            with open(self.filename_edit.text(), "r", encoding="utf-8") as file:
                data = file.read()
                self.text_edit.setPlainText(data)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notebook()
    window.show()
    sys.exit(app.exec())