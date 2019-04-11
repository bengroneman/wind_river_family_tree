import sys
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from tree import Ui_Dialog

import csv

class AppWindow(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Wind River Family Tree'
        self.initUI()

    def initUI(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(self.title)
        self.ui.toolButton.clicked.connect(self.openFileNameDialog)
        self.show()  


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;CSV Files (*.csv)", options=options)
        if fileName:
            print(fileName)
            self.get_csv_data(fileName)


    def get_csv_data(self, file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}') # First Name, Last Name, Family Name, Relationship, Relationship to
                    line_count += 1
                print(f'\t{row["First Name"]} | {row["Last Name"]} | {row["Family Name"]} | {row["Relationship"]} | {row["Relationship to"]} ')
                line_count += 1
            print(f'Processed {line_count} lines.')
            print(csv_reader)


    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)


    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
