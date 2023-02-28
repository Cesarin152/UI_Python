import sys
from PyQt5 import uic, QtWidgets
from Ui_segunda import Ui_segunda

qtCreatorFile = "principal.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
        
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.boton.clicked.connect(self.abrir)
    def abrir(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_segunda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.close()  

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())