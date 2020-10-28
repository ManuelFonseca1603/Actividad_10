from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas.particula import Particula
from particulas.adm_part import Adm_part


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.adm_part = Adm_part()    

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        #self.adm_part.mostrar()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.adm_part))    

    @Slot()
    def click_agregar(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        azul = self.ui.azul_spinBox.value()
        verde = self.ui.verde_spinBox.value()

        particula = Particula (id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.adm_part.agregar_final(particula)    

        #print(id,origen_x,origen_y,destino_x,destino_y,rojo,azul,verde)
        #self.ui.plainTextEdit.insertPlainText(id + origen_x + origen_y +
                                                 #destino_x + destino_y + rojo + azul + verde)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        azul = self.ui.azul_spinBox.value()
        verde = self.ui.verde_spinBox.value()   

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.adm_part.agregar_inicio(particula)                                            