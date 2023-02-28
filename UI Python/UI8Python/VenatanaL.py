
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
class VentanaLongitud(QMainWindow):
    
    def __init__(self, parent=None):
        super(VentanaLongitud, self).__init__(parent)
        loadUi('menu2.ui', self)
        #boton
        self.botonr.clicked.connect(self.abrirVentanaPrincipal)
        self.Lcalcular.clicked.connect(self.conversion)

    def conversion(self):
        n=float(self.Lconvertir.toPlainText())
        #La seleccion en Centimetros
        if self.icm.isChecked()==True and self.rcm.isChecked()==True:
            resultado=n*1
        if self.icm.isChecked()==True and self.rm.isChecked()==True:
            resultado=n/100
        if self.icm.isChecked()==True and self.rft.isChecked()==True:
            resultado=n*0.0328084
        #Metros
        if self.im.isChecked()==True and self.rm.isChecked()==True:
            resultado=n*1
        if self.im.isChecked()==True and self.rcm.isChecked()==True:
            resultado=n*100
        if self.im.isChecked()==True and self.rft.isChecked()==True:
            resultado=n*3.28084
        #Pies
        if self.ift.isChecked()==True and self.rcm.isChecked()==True:
            resultado=n*30.48
        if self.ift.isChecked()==True and self.rft.isChecked()==True:
            resultado=n*1
        if self.ift.isChecked()==True and self.rm.isChecked()==True:
            resultado=n*0.3048
        resultado_str=str(resultado)
        self.Lresultado.setText(resultado_str)
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()