# Подключение модулей
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QHBoxLayout, QVBoxLayout
)


# Создание главного окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Игра в города!')
window.resize(400, 200)


# Создание интерфейса
start = QLabel('Привет! Я бот, который умеет играть в города. Сыграй со мной. Готов?')
start.setStyleSheet('font: bold 18px')
button = QPushButton('Начать')
city = QLineEdit()


# Выравнивание
layout_main = QVBoxLayout()
layout_main.addWidget(start, alignment = Qt.AlignCenter)
layout_main.addWidget(city)
layout_main.addWidget(button)
window.setLayout(layout_main)
city.hide()


# Создание функций
# Функция смены экрана
def screen_change():
    button.setText('Ответить')
    city.show()
    start.setText('Москва')


#
#
#


# Функция нажатия по кнопке
def click_ok():
    if button.text() == 'Начать':
        screen_change()
    else:
        pass


button.clicked.connect(click_ok)


# Запуск приложения
window.show()
app.exec_()
