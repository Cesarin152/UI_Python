import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "raiz.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #boton
        self.calcular.clicked.connect(self.calculus)
    def calculus(self):
        import numpy as np
        p=np.zeros([3])
        p[0]=float(self.cuadratico.toPlainText())
        p[1]=float(self.lineal.toPlainText())
        p[2]=float(self.independiente.toPlainText())
        raiz_str="Su respuesta es:"+str(np.roots(p))
        self.result.setText(raiz_str)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())