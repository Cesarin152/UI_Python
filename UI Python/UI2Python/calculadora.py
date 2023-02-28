import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "calculadoradesc.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #boton
        self.CalcularButton.clicked.connect(self.calculos)
    def calculos(self):
        precio=int(self.InputPrice.toPlainText())
        desc=(self.Descuento.value())
        pago=str(precio-((desc/100)*precio))
        pagostr="Su pago es "+pago
        self.Result.setText(pagostr)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())