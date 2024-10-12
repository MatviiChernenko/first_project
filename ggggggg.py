from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QMessageBox, QHBoxLayout

app = QApplication([])
app.setStyleSheet("QLabel {font-size:16px}")
widget = QWidget()
widget.setWindowTitle("Конкурс від Crazy People")
widget.resize(450,300)
widget.move(500,300)

text = QLabel("В якому році канал  отримав золоту кнопку від YouTube")
rb1 = QRadioButton("2018")
rb2 = QRadioButton("2020")
rb3 = QRadioButton("2015")
rb4 = QRadioButton("2005")

v_line = QHBoxLayout()
v_line.addWidget(rb1, alignment = Qt.AlignCenter)
v_line.addWidget(rb2, alignment = Qt.AlignCenter)

v_line1 = QHBoxLayout()
v_line1.addWidget(rb3, alignment = Qt.AlignCenter)
v_line1.addWidget(rb4, alignment = Qt.AlignCenter)

v_line2 = QVBoxLayout()
v_line2.addWidget(text, alignment = Qt.AlignCenter)
v_line2.addLayout(v_line)
v_line2.addLayout(v_line1)

widget.setLayout(v_line2)

def win():
    qm = QMessageBox()
    qm.setText("You win")
    qm.exec_()

def lose():
    qm = QMessageBox()
    qm.setText("You lose")
    qm.exec_()

rb1.clicked.connect(lose)
rb2.clicked.connect(lose)
rb3.clicked.connect(win)
rb4.clicked.connect(lose)

widget.show()
app.exec_()
