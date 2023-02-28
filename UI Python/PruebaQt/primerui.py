#from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from Ui_prueba import  Ui_MainWindow

class Prueba(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Prueba,self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #boton
        self.calcular.clicked.connect(self.calcularDesc)
    def calcularDesc(self):
        Pre=int(self.precio.toPlainText())#Escanear el valor de entrada de la cajita
        pre2=Pre
        Desc=int(self.descuento.value())
        calcularDesc=Pre-pre2*(Desc/100)
        str_desc=str(calcularDesc)
        self.resultado.setText(str_desc)

import sys    
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Prueba()#Creacion de objeto
    main.show()
    sys.exit(app.exec_())   