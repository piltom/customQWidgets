# customQWidgets
Funky stuff to make a GUI fast using widget tables and keywords with pyqt5.
# Example
The basic usage of the module is shown in the example. There, a small gui with a table widget and a set of control buttons is implemented. This is done through creating a 2d list of QWidgets and special strings.
Clicking the open dialog button will prompt a dialog that asks the user for information. This dialog is created using a table of cQCustomInput (which can take a number range, a string list or a default string as arguments) and strings (which are converted to labels). cQCustomInput morphs based on the arguments pased. The dialog will return then a status and a list of the values chosen. Numbers and free text input are returned as their values, but for the string list, the index of the selected item is returned.

# Todo
Develop a way of setting properties easily, such as stretching factors, connecting signals all at once, etc...
