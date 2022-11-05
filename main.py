import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import ctypes
from logica.Modulacion_por_desplazamiento import Ondas
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QLineEdit, QInputDialog)

class Ventana_principal(QMainWindow):


    def __init__(self):

        QMainWindow.__init__(self)
        #super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Principal.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        self.instancia = Ondas()
        self.btn_ask.clicked.connect(self.funcionAsk)
        self.btn_fsk.clicked.connect(self.funcionFsk)
        self.btn_psk.clicked.connect(self.funcionPsk)
        self.btn_cuatro_psk.clicked.connect(self.funcion_cuatroPsk)
        self.btn_ochoqam.clicked.connect(self.funcionOchoQam)
        self.btn_unipolar.clicked.connect(self.funcionUnipolar)
        self.btn_nrzl.clicked.connect(self.funcionNrz_l)
        self.btn_nrzi.clicked.connect(self.funcionNrz_i)
        self.btn_rz.clicked.connect(self.funcionRz)
        self.btn_manchester.clicked.connect(self.funcionManchester)
        self.btn_manchester_diff.clicked.connect(self.funcionManchester_diff)
        self.btn_ami.clicked.connect(self.funcionAmi)
        self.btn_b.clicked.connect(self.funcionB8zs)
        self.btn_hd.clicked.connect(self.funcionHdb3)
        self.btn_analogico.clicked.connect(self.funcionAnalogico_digital)



    
    def funcionAsk(self):
        try:
            texto,ok = QInputDialog.getText(self, "ASK", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.ASK(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)

    def funcionFsk(self):
        try:
            texto,ok = QInputDialog.getText(self, "FSK", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.FSK(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)

    def funcionPsk(self):
        try:
            texto,ok = QInputDialog.getText(self, "PSK", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.PSK(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)

    def funcion_cuatroPsk(self):
        try:
            texto,ok = QInputDialog.getText(self, "4-PSK", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.cuatro_PSK(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)
                
    def funcionOchoQam(self):
        try:
            texto,ok = QInputDialog.getText(self, "8-QAM", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.ocho_QAM(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)

    def funcionUnipolar(self):
        try:
            texto,ok = QInputDialog.getText(self, "Unipolar", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.unipolar(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)
                    
    def funcionNrz_l(self):
        try:
            texto,ok = QInputDialog.getText(self, "NRZ-L", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.NRZ_L(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)
    
    def funcionNrz_i(self):
        try:
            texto,ok = QInputDialog.getText(self, "NRZ-I", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.NRZ_I(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)

    def funcionRz(self):
        try:
            texto,ok = QInputDialog.getText(self, "RZ", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.RZ(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)
   
    def funcionManchester(self):
        try:
            texto,ok = QInputDialog.getText(self, "Manchester", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.Manchester(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)
    
    def funcionManchester_diff(self):
        try:
            texto,ok = QInputDialog.getText(self, "Manchester diferencial", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.Manchester_diff(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)
    
    def funcionAmi(self):
        try:
            texto,ok = QInputDialog.getText(self, "AMI", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.AMI(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)

    def funcionB8zs(self):
        try:
            texto,ok = QInputDialog.getText(self, "B8ZS", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.B8ZS(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!","Ha ocurrido un error", QMessageBox.Discard)

    def funcionHdb3(self):
        try:
            texto,ok = QInputDialog.getText(self, "NRZ-L", "Dame la palabra que desees convertir:")
            if(ok and len(texto) > 0):
                self.instancia.HDB3(texto)
        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar letras en el recuadro", QMessageBox.Discard)
                print(e)

    def funcionAnalogico_digital(self):

        try:

            cantidad,ok = QInputDialog.getInt(self, "Analogico a digital", "Cuantos numeros quieres poner:")

            if(ok and cantidad > 0):
                numeros = []
                contador = 0

                while(len(numeros) < cantidad):
                    numero,ok = QInputDialog.getInt(self, "Numeros" , "Dame el numero en la posicion "+str(contador+1))
                    if(ok):
                        numeros.append(numero)

                if(len(numeros)>0):
                    self.instancia.Analogica_digital(numeros)

        except Exception as e:
                QMessageBox.warning(self, "hey !!", "Debes colocar todos los numeros", QMessageBox.Discard)
                print(e)

    def showDialogInt(self,titulo,mensaje):

        numero, ok = QInputDialog.getInt(self, titulo, mensaje) 

        return numero,ok


if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Ventana_principal()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()