import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "ope.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.checksuma.stateChanged.connect(self.cambio)
        self.checkresta.stateChanged.connect(self.cambio)
    def cambio(self):
        n1=int(self.num1.toPlainText())
        n2=int(self.num2.toPlainText())
        if self.checksuma.isChecked()==True:
            suma=n1+n2
            resultado_str=str(suma)
            self.Result.setText(resultado_str)
        elif self.checkresta.isChecked()==True:
            resta=n1-n2
            resultado_str=str(resta)
            self.Result.setText(resultado_str)  
        else:
            self.Result.setText("")
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())