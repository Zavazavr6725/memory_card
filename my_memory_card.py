from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup, QMessageBox

class Questions():
    def __init__(self, quest, r_a, w1, w2, w3):
        self.question = quest
        self.right_answ = r_a
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3



def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    answer_button.setText('Следующий вопрос')

def show_question():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    answer_button.setText('Ответить')
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)


def start_test():
    if answer_button.text() == 'Ответить':
        chek_answer()
    else:
        next_questions()

def ask(q):
    shuffle(answer)
    text.setText(q.question)
    answer[0].setText(q.right_answ)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    correct_answer.setText(q.right_answ)
    show_question()


def chek_answer():

    if answer[0].isChecked():
        answer_result.setText('Правильно!')
        result.score += 1

    else:
        answer_result.setText('Неправильно!')
    show_result()


def next_questions():
    main_window.score_quest += 1

    if main_window.score_quest >= len(Questions_list):
        main_window.score_quest = 0
        result.setText('Ваш результат\n' + str(result.score) + '/' + str(len(Questions_list)))
        result.exec_()
        result.score = 0
    ask(Questions_list[main_window.score_quest])


app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Memory Card')
main_window.resize(400, 300)
main_window.score_quest = -1
result = QMessageBox()
result.setWindowTitle('Rезультат')
result.score = 0
text = QLabel('Какой национальности не существует?')  
RadioGroupBox = QGroupBox('Варианты ответов')
button1 = QRadioButton('Энцы')
button2 = QRadioButton('Чулымцы')
button3 = QRadioButton('Смурфы')
button4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)
answer = [button1, button2, button3, button4]
answer_button = QPushButton('Ответить')
AnswerGroupBox = QGroupBox('Результаты теста')
answer_result = QLabel('Правильно/неправильно')
correct_answer = QLabel('Праивльный ответ')

main_Layout = QVBoxLayout()
line_text = QHBoxLayout()
line_answer = QHBoxLayout()
layout_buttonH1 = QHBoxLayout()
layout_buttonH2 = QHBoxLayout()
mainLayout_buttonV = QVBoxLayout()
layout_answer = QVBoxLayout()

layout_answer.addWidget(answer_result, alignment = Qt.AlignLeft)
layout_answer.addWidget(correct_answer, alignment = Qt.AlignCenter)
layout_buttonH1.addWidget(button1, alignment = Qt.AlignCenter)
layout_buttonH1.addWidget(button2, alignment = Qt.AlignCenter)
layout_buttonH1.setSpacing(70)
layout_buttonH2.addWidget(button3, alignment = Qt.AlignCenter)
layout_buttonH2.addWidget(button4, alignment = Qt.AlignCenter)
layout_buttonH2.setSpacing(70)
mainLayout_buttonV.addLayout(layout_buttonH1)
mainLayout_buttonV.addLayout(layout_buttonH2)
mainLayout_buttonV.setSpacing(35)
RadioGroupBox.setLayout(mainLayout_buttonV)
AnswerGroupBox.setLayout(layout_answer)
main_Layout.addWidget(text,20, alignment = Qt.AlignCenter)
main_Layout.addWidget(RadioGroupBox, 40)
main_Layout.addWidget(AnswerGroupBox, 40)
main_Layout.addWidget(answer_button, 40)
main_window.setLayout(main_Layout)

AnswerGroupBox.hide()

Questions_list = [Questions('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Алеуты', 'Чулымцы'),
 Questions('Что в чемодане?', 'бипки', 'ласты', 'гвозди', 'арбузы'),
 Questions('Что попросил сын у отца?', 'парты', 'конфеты', 'кашу', 'мячик'), ]

next_questions()
answer_button.clicked.connect(start_test)

main_window.show()
app.exec_()

