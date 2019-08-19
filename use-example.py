from customQWidgets import cQWidgetTableGB, cQCustomInput, cQWidgetTable
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QLabel, QPushButton
import sys

def connect():
    print("dummy")
def start():
    print("dummy")
def stop():
    print("dummy")
def cancel():
    print("dummy")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('Button box')

buttonTable=[[          QPushButton("Connect")            ],
             [QPushButton("Start"),  QPushButton("Stop")  ],
             [       "span"      , QPushButton("Cancel") ]]
buttonTable[0][0].clicked.connect(connect)
buttonTable[0][0].setMaximumSize(1000,1000)
buttonTable[1][0].clicked.connect(start)
buttonTable[1][0].setMaximumSize(1000,1000)
buttonTable[1][1].clicked.connect(stop)
buttonTable[1][1].setMaximumSize(1000,1000)
buttonTable[2][1].clicked.connect(cancel)
buttonTable[2][1].setMaximumSize(1000,1000)

buttonsWidget=cQWidgetTableGB(buttonTable, "Control")


centralWidgetTable=[[QTableWidget(), buttonsWidget],
                         [  "span"   , "empty"]]
                  
centralWidget=cQWidgetTable(centralWidgetTable, window)
window.setCentralWidget(centralWidget)
window.show()
sys.exit(app.exec_())