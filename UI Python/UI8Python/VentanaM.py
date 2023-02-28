
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
class VentanaMasa(QMainWindow):
    
    def __init__(self, parent=None):
        super(VentanaMasa, self).__init__(parent)
        loadUi('menu3.ui', self)
        self.botonr.clicked.connect(self.abrirVentanaPrincipal)
        self.Mcalcular.clicked.connect(self.conversion)
        
    def conversion(self):
        n=float(self.Mconvertir.toPlainText())
        if self.ikg.isChecked()==True and self.rkg.isChecked()==True:
            resultado=n*1
        if self.ikg.isChecked()==True and self.rg.isChecked()==True:
            resultado=n*1000
        if self.ikg.isChecked()==True and self.rlb.isChecked()==True:
            resultado=n*2.20462
        if self.ilb.isChecked()==True and self.rlb.isChecked()==True:
            resultado=n*1
        if self.ilb.isChecked()==True and self.rkg.isChecked()==True:
            resultado=n*0.453592
        if self.ilb.isChecked()==True and self.rg.isChecked()==True:
            resultado=n*453.592
        if self.ig.isChecked()==True and self.rg.isChecked()==True:
            resultado=n*1
        if self.ig.isChecked()==True and self.rkg.isChecked()==True:
            resultado=n/1000
        if self.ig.isChecked()==True and self.rlb.isChecked()==True:
            resultado=n*0.00220462
        resultado_str=str(resultado)
        self.Mresultado.setText(resultado_str)    
    

    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()