from customQWidgets import cQWidgetTableGB, cQCustomInput, cQWidgetTable, cQConfigDialog
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QLabel, QPushButton
import sys

def opendialog():
  options=["beef", "tuna", "bacon"]
  comFormWidgets=[["Dropdown", cQCustomInput(arg_optionList=options,  arg_defaultValue=2, parent=None)],
                  ["Number",   cQCustomInput(arg_numberRange=[0,100], arg_defaultValue=50,parent=None)],
                  ["Text",     cQCustomInput(arg_defaultValue="default text", parent=None)]]
  
  info, ok=cQConfigDialog.promptDialog(arg_settings=comFormWidgets)
  if(ok):
    print("Dropdown: %s" % options[info[0]])
    print("Number: %i" % info[1])
    print("Text: %s" % info[2])
def start():
  print("dummy")
def stop():
    print("dummy")
def cancel():
    print("dummy")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('Button box')

buttonTable=[[          QPushButton("Open dialog")        ],
             [QPushButton("Start"),  QPushButton("Stop")  ],
             [       "span"      , QPushButton("Cancel") ]]
buttonTable[0][0].clicked.connect(opendialog)
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