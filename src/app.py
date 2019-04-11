import sys
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from tree import Ui_Dialog

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
        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
        self.show()  


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)


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
