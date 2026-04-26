# write the code for main app and first screen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from second_win import *

#------DATA-------

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Welcome to the Health status detection program!'
txt_next = 'Start'
txt_instruction = ('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
                   'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n'
                   'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds; \n'
                   'then, within 45 seconds, the subject performs 30 squats.\n'
                   'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
                   'and then for the last 15 seconds of the first minute of the recovery period.\n'
                   'Important! If you feel unwell during the test (dizziness,\n'
                   'tinnitus, shortness of breath, etc.), stop the test and consult a physician.' )
txt_title = 'Health'
txt_name = 'Enter Your full name:'
txt_hintname = "Full name"
txt_hintage = "0"
txt_test1 = 'Lie on your back and take your pulse for 15 seconds. Click the "Start first test" button to start the timer.\nWrite down the result in the appropriate field.'
txt_test2 = 'Perform 30 squats in 45 seconds. To do this, click the "Start doing squats" button\nto start the squat counter.'
txt_test3 = 'Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute.\nPress the "Start final test" button to start the timer.\nThe seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields.'
txt_sendresults = 'Send the results'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Start the first test'
txt_starttest2 = 'Start doing squats'
txt_starttest3 = 'Start the final test'
txt_timer = ''


txt_age = 'Full years:'
txt_finalwin = 'Results'
txt_index = 'Roufier Index: '
txt_workheart = 'Cardiac performance: '

#------CLASS-----

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction =QLabel(txt_instruction)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()
        
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
#-----END/RUNAPP----
app = QApplication([])
mw = MainWin()
app.exec_()

