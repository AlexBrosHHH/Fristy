# Библиотеки
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import pyttsx3
from gpt_api import GPT
# Импорт файла с дизайном
from gpt_design import Ui_MainWindow
# Распознование и озвука
class Assistant:
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.gpt =  GPT()
        # Настройки
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('value', 0.9)

    # Распознование
    def listen(self):
        while True:
            with sr.Microphone() as source:
                print('Говорите: ')
                audio = self.r.listen(source) 
            try:
                text = self.r.recognize_google(audio, language='ru-RU')
                yield text
            except sr.UnknownValueError:
                print('Речь не распознона')
            except sr.RequestError:
                print('Ошибка сервер.')
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    def run(self):
        for task in self.listen():
            answer = self.gpt.request(task)
            self.say(answer)
if __name__ == '__main__':
    fristy = Assistant()
    fristy.run()




# Базовая конструкция
class gpt_bot(QtWidgets.QMainWindow):
    def __init__(self):
        super(gpt_bot, self).__init__()
        self.gpt_design = Ui_MainWindow()
        self.gpt_design.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Фристи Ассиситент (GPT VERSION)     v1.0')



# Отображение Окна
app = QtWidgets.QApplication([])
application = gpt_bot()
application.show()


# Закрытие окна
sys.exit(app.exec())