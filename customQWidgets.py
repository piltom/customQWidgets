###############################################################################
#                                                                             #
# Custom QWidgets and Useful functions for generating QWidgets from common    #
# datatypes and other QWidgets.                                               #
#                                                                             #
# Author: Tomas Alvarez Vanoli, tomiav97@gmail.com                            #
# Latest update:   16/jul/2019                                                #
# License: Apache License 2.0
###############################################################################

from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QDialog, QLabel, QComboBox, QDialogButtonBox,QSpinBox, QLineEdit, QSpacerItem, QSizePolicy, QPlainTextEdit, QPushButton, QCheckBox
from PyQt5.QtCore import pyqtSignal
##############################################################################
# 1. Functions
##############################################################################

def list2QCBox(arg_list, arg_index=0,parent=None):
  cb=QComboBox(parent)
  cb.addItems(map(str,arg_list))
  cb.setCurrentIndex(arg_index)
  return cb



def addGroupBox2Widget(arg_widget, arg_title="", parent=None):
  gb=QGroupBox(arg_title,parent);
  arg_widget.setParent(gb)
  gb.setLayout(QGridLayout())
  gb.layout().addWidget(arg_widget)
  return gb

##############################################################################
# 2. Custom QWidget Classes (cQ prefix)
##############################################################################

class cQLogConsole(QWidget):
  save=pyqtSignal()
  def __init__(self,parent):
    super(cQLogConsole, self).__init__(parent)
    self.widgetTable=[[QPlainTextEdit()],
                      [QPushButton("Save"), QPushButton("Clear"),QCheckBox("Hide")]]
    self.widgetTable[1][0].clicked.connect(self.save.emit)
    self.widgetTable[1][1].clicked.connect(self.widgetTable[0][0].clear)
    self.widgetTable[1][2].toggled.connect(self.cbToggled)
    self.widgetTable[0][0].setReadOnly(True)
    super().setLayout(QGridLayout())
    super().layout().addWidget(self.widgetTable[0][0],0,0,1,3)
    super().layout().addWidget(self.widgetTable[1][0],1,0)
    super().layout().addWidget(self.widgetTable[1][1],1,1)
    super().layout().addWidget(self.widgetTable[1][2],1,2)
  def cbToggled(self):
    self.widgetTable[0][0].setVisible(not self.widgetTable[1][2].isChecked())
  def log(self, entry):
    self.widgetTable[0][0].appendPlainText(entry)

#Can contain different input widgets, and the data in them obtained through the same function
# TODO add generic signal for value change
class cQCustomInput(QWidget):
  def __init__(self, arg_optionList=None, arg_numberRange=None, arg_defaultValue=None, parent=None):
    super(cQCustomInput, self).__init__(parent)
    self.inputType=None
    self.widget=None
    super().setLayout(QGridLayout())
    if(type(arg_optionList)==list):
      if(type(arg_defaultValue)!=int):
        arg_defaultValue=0
      self.widget=list2QCBox(arg_optionList, arg_defaultValue, parent)
      super().layout().addWidget(self.widget)
      self.inputType=1
    elif(type(arg_numberRange)==list):
      if(type(arg_defaultValue)!=int):
        arg_defaultValue=arg_numberRange[0]
      self.widget=QSpinBox(parent)
      self.widget.setValue(arg_defaultValue)
      self.widget.setMinimum(arg_numberRange[0])
      self.widget.setMaximum(arg_numberRange[1])
      self.widget.setWrapping(True)
      super().layout().addWidget(self.widget)
      self.inputType=2
    else:
      self.widget=QLineEdit(parent)
      self.widget.setText(str(arg_defaultValue))
      super().layout().addWidget(self.widget)
      self.inputType=3
  def getInput(self):
    if(self.inputType==1):
      return self.widget.currentIndex()
    elif(self.inputType==2):
      return self.widget.value()
    else:
      return self.widget.text()
  def getWidget(self):
    return self.widget

#Builds a widget with a grid layout based on the table of widgets passed as arg_widgetTable
#the widget at row,col postition can be obtained with getWidget(row,col)
class cQWidgetTable(QWidget):
  def __init__(self, arg_widgetTable, parent = None):
    super(cQWidgetTable, self).__init__(parent)
    self.widgetTable=arg_widgetTable
    super().setLayout(QGridLayout())
    
    self.width=0
    for row in range(0,len(self.widgetTable)):
      for col in range(0,len(self.widgetTable[row])):
        if(len(self.widgetTable[row])>self.width):
          self.width=len(self.widgetTable[row])

    for row in range(0,len(self.widgetTable)):
      for col in range(0,len(self.widgetTable[row])):
        if(type(self.widgetTable[row][col])!=str):
          self.widgetTable[row][col].setParent(self)
          rowspan=1
          try:
            while(self.widgetTable[row+rowspan][col]=='span'):
              rowspan+=1
          except:
            pass
          colspan=int(self.width/len(self.widgetTable[row]))
          super().layout().addWidget(self.widgetTable[row][col],row,col,rowspan,colspan)
        elif(self.widgetTable[row][col]=='empty'):
          super().layout().addItem(QSpacerItem(1, 1),row,col)
  def getWidget(self, arg_row, arg_col):
    return self.widgetTable[arg_row][arg_col]
  def setWidget(self, arg_widget, arg_row, arg_col):
    self.widgetTable[arg_row][arg_col]=arg_widget


#Like cQWidgetTable but contained within a QGroupBox. New argument: arg_title: The title of the group box
class cQWidgetTableGB(QWidget):
  def __init__(self, arg_widgetTable,arg_title="", parent = None):
    super(cQWidgetTableGB, self).__init__(parent)
    self.widgetTable=arg_widgetTable
    super().setLayout(QGridLayout())
    gb=QGroupBox(arg_title,self)
    gb.setLayout(QGridLayout())
    
    self.width=0
    for row in range(0,len(self.widgetTable)):
      for col in range(0,len(self.widgetTable[row])):
        if(len(self.widgetTable[row])>self.width):
          self.width=len(self.widgetTable[row])
    
    for row in range(0,len(self.widgetTable)):
        for col in range(0,len(self.widgetTable[row])):
          print("row %d col %d" % (row, col))
          if(type(self.widgetTable[row][col])!=str):
            self.widgetTable[row][col].setParent(self)
            rowspan=1
            try:
              while(self.widgetTable[row+rowspan][col]=='span'):
                rowspan+=1
            except:
              pass
            colspan=int(self.width/len(self.widgetTable[row]))
            gb.layout().addWidget(self.widgetTable[row][col],row,col,rowspan,colspan)
          elif(self.widgetTable[row][col]=='empty'):
            super().layout().addItem(QSpacerItem(1, 1),row,col)
    super().layout().addWidget(gb)
  
  def getWidget(self, arg_row, arg_col):
    return self.widgetTable[arg_row][arg_col]
  def setWidget(self, arg_widget, arg_row, arg_col):
    self.widgetTable[arg_row][arg_col]=arg_widget


#Based on the table defined in arg_settings, this class implements a configuration dialog (opened with promptDialog). It returns a data array
#with the order of the inputs in the arg_settings table (left to right, top to bottom).
#arg_settings should be a table with either strings (will appear as labels) or objects of the type cQCustomInput (which has a standarized function for getting the data)
class cQConfigDialog(QDialog):
  def __init__(self, arg_settings=[], parent = None):
    super(cQConfigDialog, self).__init__(parent)
    layout = QGridLayout(self)
    self.comFormWidgets=arg_settings
    #map where the inputs are (this considers anything not a string an input)
    self.inputMap=[]
    for row in range(0,len(self.comFormWidgets)):
      for col in range(0, len(self.comFormWidgets[row])):
        if(type(self.comFormWidgets[row][col])!=str):
          self.inputMap.append([row,col])                                            #If it's an input type, map it as so
        else:
          self.comFormWidgets[row][col]=QLabel(self.comFormWidgets[row][col],None)   #If it's not, then set it as a label

    self.comFormWidgets.append((QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=self),))
    self.widget=cQWidgetTable(self.comFormWidgets, self)
    layout.addWidget(self.widget)
    self.widget.getWidget(len(self.comFormWidgets)-1,0).accepted.connect(self.accept)
    self.widget.getWidget(len(self.comFormWidgets)-1,0).rejected.connect(self.reject)
    # get conf info
  def informacion(self):
    retlist=[]
    for xy in self.inputMap:
      retlist.append(self.comFormWidgets[xy[0]][xy[1]].getInput())
    return retlist
  # static method to create the dialog and return info
  @staticmethod
  def promptDialog(arg_settings=[],parent = None):
      dialog = cQConfigDialog(arg_settings,parent)
      result = dialog.exec_()
      info = dialog.informacion()
      return (info, result == QDialog.Accepted)
