from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup

from random import *

app = QApplication([]) 
main_win = QWidget() 
main_win.setWindowTitle('Конкурс от Crazy People') 
main_win.resize(400, 200)
qwerty = QPushButton('кнпк впрйд бр')

qwertyuiop = QLabel('ъъъъъъъъъ')

RadioGroupBox = QGroupBox('asdfghj')
o_1 = QRadioButton('w')
o_2 = QRadioButton('ю')
o_3 = QRadioButton('wi')
o_4 = QRadioButton('g')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(o_1)
layout_ans2.addWidget(o_2)
layout_ans3.addWidget(o_3)
layout_ans3.addWidget(o_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

buutonGruppe = QButtonGroup()
buutonGruppe.addButton(o_1)
buutonGruppe.addButton(o_2)
buutonGruppe.addButton(o_3)
buutonGruppe.addButton(o_4)





RadioGroupBox.setLayout(layout_ans1)

layout_1 = QHBoxLayout()
layout_1.addWidget(qwertyuiop)
layout_2 = QHBoxLayout()
layout_2.addWidget(RadioGroupBox)
layout_3 = QHBoxLayout()
layout_3.addWidget(qwerty)

RadioGroupBox.hide()
EntGrupps = QGroupBox('результаты')
Sadn = QLabel('правильно/неправильно')

Coldm = QLabel('правильный ответ/неправильный ответ')

layout_5 = QVBoxLayout()
layout_5.addWidget(Sadn)
layout_5.addWidget(Coldm)


EntGrupps.setLayout(layout_5)





layout_4 = QVBoxLayout()
layout_4.addLayout(layout_1)
layout_4.addLayout(layout_2)
layout_4.addWidget(EntGrupps)
layout_4.addLayout(layout_3)

main_win.setLayout(layout_4)

def show_result():
    RadioGroupBox.hide()
    EntGrupps.show()
    qwerty.setText('кнпк нзд бр')

def show_question():
    EntGrupps.hide()
    RadioGroupBox.show()
    qwerty.setText('кнпк впрйд бр')

    buutonGruppe.setExclusive(False)
    o_1.setChecked(False)
    o_2.setChecked(False)
    o_3.setChecked(False)
    o_4.setChecked(False)
    buutonGruppe.setExclusive(True)

def start_test():
    if qwerty.text() == ('кнпк нзд бр'):
        show_question()
    else:
        show_result()

class Question():
    def __init__(self, wrong1, wrong2, wrong3, question, right_answer):
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.right_answer = right_answer
        self.question = question
    



















question_list = []
q1 = Question('y', 'w', 'z', '23232323-56567889', 'x')

question_list.append(q1)

q5 = Question('w', 'k ', 'o', '963+(-5688)', 'g')

question_list.append(q5)



q2 = Question('р', 'g ', 'u', '234567*2', '469134')

question_list.append(q2)


q3 = Question('1497', '-1456', '1488', '744*2', 'пасхалко')

question_list.append(q3)



q4 = Question('0', '-354678789', '88827064', '88888888+89274', '88978162')

question_list.append(q4)


q6  = Question('х', '637', '43434', '2+2-5', '0-1')

question_list.append(q6)


q7 = Question('6', '4', '3', '2+2', '22')

question_list.append(q7)









answer = [o_1, o_2, o_3, o_4]
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    qwertyuiop.setText(q.question)
    Sadn.setText(q.right_answer)
    show_question()


def show_correct(res):
    Coldm.setText(res)
    show_result()








def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answer[1].isChecked() or answer[2].isChecked or answer[3].isChecked():
            show_correct('Неверно!')


q=Question('какой-то вопрос','йцу','фыв','ячс','проол')
ask(q)


def next_question():
    cur_question = randint(0, len(question_list) - 1)
        
    ask(question_list[cur_question])
    main_win.total += 1
    print('Статистика верных ответов и заданных вопросов')
    print('количетво вопросов', main_win.total)
    print('количество ответов', main_win.score)
    print('рейтинг', main_win.score/main_win.total * 100)






def click_OK():
    if qwerty.text() == 'кнпк впрйд бр':
        check_answer()
    else:
        next_question()









main_win.cur_question = -1
qwerty.clicked.connect(click_OK)
main_win.total = 0
main_win.score = 0
main_win.show()
app.exec_()




