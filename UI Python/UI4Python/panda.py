import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from g2 import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        #Aquí​ van los botones
        self.boton1.clicked.connect(self.getCSV)
        self.boton2.clicked.connect(self.plot)
        self.boton3.clicked.connect(self.estadisticas)
    #Aquí​ van las nuevas funciones
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\cesar\\OneDrive\\Documentos\\Interfaz Grafica\\UI4Python')
        if filePath != "":
            print ("Dirección",filePath) #Opcional​ imprimir la dirección del archivo
            self.df = pd.read_csv(str(filePath))
            self.combox.addItems(list(self.df.columns.values))
            self.comboy.addItems(list(self.df.columns.values))
            self.comboes.addItems(list(self.df.columns.values))
    def plot(self):
        x=self.df[str(self.combox.currentText())]#Utiliza el texto actual del combo
        y=self.df[str(self.comboy.currentText())]
        plt.plot(x,y)
        plt.show()
        self.combox.clear()
        self.comboy.clear()
        
    def estadisticas(self):
        estadistica="Estadistica de col2: "+str(self.comboes.currentText())+"-----"+str(self.df[self.comboes.currentText()].describe())
        self.result.setText(estadistica)
        self.comboes.clear()
    #Esta​ función abre el archivo CSV    
    
    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())