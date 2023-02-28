import sys
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5 import uic, QtWidgets

qtCreatorFile = "exc.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.importar.clicked.connect(self.getxls)
        self.estadis.clicked.connect(self.estadisticas)
        self.graficar.clicked.connect(self.plot)

    def getxls(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/karris/python')
        if filePath != "":
            self.datos=pd.ExcelFile(str(filePath))
            self.combox.addItems(list(self.datos.sheet_names))#apartir de las nombres de las hojas de excel se creara una lista
            self.df=self.datos.parse(self.combox.currentText())
            self.comboy.addItems(list(self.df.columns.values))
    def plot (self):
        self.df=self.datos.parse(self.combox.currentText())
        x=self.df['x']
        y=self.df['y']
        plt.plot(x,y)
        plt.show()
        
    def estadisticas(self):
        self.df=self.datos.parse(self.combox.currentText())  
        estad_st=" Estadisticas de la columna"+str(self.comboy.currentText())+"\n"+str(self.df[self.comboy.currentText()].describe())
        self.result.setText(estad_st)
        
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())