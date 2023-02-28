import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from VenatanaL import VentanaLongitud
from VentanaM import VentanaMasa

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('menu1.ui', self)
        #Check Box
        self.masa.stateChanged.connect(self.abrirVentanaMasa)
        self.longitud.stateChanged.connect(self.abrirVentanaLongitud)
    def abrirVentanaMasa(self):
        self.hide()
        otraventana=VentanaMasa(self)
        otraventana.show()
    def abrirVentanaLongitud(self):
        self.hide()
        otraventana=VentanaLongitud(self)
        otraventana.show()

        


app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())