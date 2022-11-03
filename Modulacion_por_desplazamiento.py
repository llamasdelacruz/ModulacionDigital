import numpy as np
import math as m
import matplotlib.pyplot as plt
from Palabras_binarias import PalabrasBinarias


class Ondas(PalabrasBinarias):

    def Graficar_onda(self, direcion_ondas, amplitud_onda1, frecuencia_onda1, amplitud_onda2, frecuencia_onda2, cambio_fase, oracion, titulo):

        base = 0
        tope = 1
        color_1 = 0.5
        color_0 = 0.5
        array = self.Convertir_binario(oracion)
        direccion = direcion_ondas
        bit_anterior = array[0][:1]
        for trama in array:
            for bit in trama:

                if(bit == "1"):

                    if(cambio_fase):
                        if(bit_anterior != "1" and direccion == 1):
                            direccion = -1
                        elif(bit_anterior != "1" and direccion == -1):
                            direccion = 1

                    x = np.linspace(base*np.pi, tope*np.pi, 100)
                    y = direccion*amplitud_onda1*np.sin(x*frecuencia_onda1)
                    plt.plot(x, y, color='black', alpha=color_1)

                    color_1 = 1 if color_1 == 0.5 else 0.5

                else:
                    if(cambio_fase):
                        if(bit_anterior != "0" and direccion == 1):
                            direccion = -1
                        elif(bit_anterior != "0" and direccion == -1):
                            direccion = 1

                    x2 = np.linspace(base*np.pi, tope*np.pi, 100)
                    y2 = direccion*amplitud_onda2*np.sin(x2*frecuencia_onda2)
                    plt.plot(x2, y2, color='green', alpha=color_0)
                    color_0 = 1 if color_0 == 0.5 else 0.5

                base = tope
                tope += 1
                bit_anterior = bit

        plt.axhline(y=0, color="black")
        plt.grid(axis='x', color='0.95')
        plt.title(titulo)
        # plt.title('ASK Modulación por dezplazamiento de amplitud')
        plt.show()

    def ASK(self):
        frase = input("Dame la palabra que quieres:")
        self.Graficar_onda(direcion_ondas=-1,
                           amplitud_onda1=4,
                           frecuencia_onda1=2,  # la onda 1 se refiere a la onda de 1 y la onda 2 es la onda del cero
                           amplitud_onda2=1,
                           frecuencia_onda2=2,
                           cambio_fase=False,
                           oracion=frase,
                           titulo='ASK Modulación por dezplazamiento de amplitud'
                           )

    def FSK(self):
        frase = input("Dame la palabra que quieres:")
        self.Graficar_onda(direcion_ondas=-1,
                           amplitud_onda1=2,
                           frecuencia_onda1=6,
                           amplitud_onda2=2,
                           frecuencia_onda2=1,
                           cambio_fase=False,
                           oracion=frase,
                           titulo='FSK Modulación por dezplazamiento de frecuencia'
                           )

    def PSK(self):
        frase = input("Dame la palabra que quieres:")
        self.Graficar_onda(direcion_ondas=1,
                           amplitud_onda1=1,
                           frecuencia_onda1=2,
                           amplitud_onda2=1,
                           frecuencia_onda2=2,
                           cambio_fase=True,
                           oracion=frase,
                           titulo='PSK Modulación por dezplazamiento de fase'
                           )

    def cuatro_PSK(self):
        oracion = input("Dame la palabra que quieres:")
        base = 0
        tope = 1
        array = self.Convertir_binario(oracion)
        for trama in array:
            for i in range(2, 9, 2):

                bites = trama[i-2:i]

                if(bites == "01"):

                    x = np.linspace(base*np.pi, tope*np.pi, 100)
                    y = np.cos(x*2)
                    plt.plot(x, y, color='black')

                elif(bites == "10"):

                    x = np.linspace(base*np.pi, tope*np.pi, 100)
                    y = -1*np.sin(x*2)
                    plt.plot(x, y, color='grey')

                elif(bites == "11"):

                    x = np.linspace(base*np.pi, tope*np.pi, 100)
                    y = -1*np.cos(x*2)
                    plt.plot(x, y, color='blue')

                elif(bites == "00"):

                    x2 = np.linspace(base*np.pi, tope*np.pi, 100)
                    y2 = np.sin(x2*2)
                    plt.plot(x2, y2, color='blue', alpha=0.5)

                base = tope
                tope += 1

        plt.axhline(y=0, color="black")
        plt.grid(axis='x', color='0.95')
        plt.title("4-PSK")
        # plt.title('ASK Modulación por dezplazamiento de amplitud')
        plt.show()

    def ocho_QAM(self):
        oracion = input("Dame la palabra que quieres:")
        base = 0
        tope = 1
        array = self.Convertir_binario(oracion)
        trama_completa = self.trama_preparar_QAM(array)

        for i in range(3, len(trama_completa)+3, 3):

            bites = trama_completa[i-3:i]

            if(bites == "101"):

                x = np.linspace(base*np.pi, tope*np.pi, 100)
                y = -2*np.sin(x*2)
                plt.plot(x, y, color='black')

            elif(bites == "100"):

                x = np.linspace(base*np.pi,tope*np.pi,100)
                y = -1*np.sin(x*2)
                plt.plot(x, y, color='grey')
            
            elif(bites == "001"):

                x = np.linspace(base*np.pi,tope*np.pi,100)
                y = 2*np.sin(x*2)
                plt.plot(x, y, color='blue')

            elif(bites == "000"):
                    
                x2 = np.linspace(base*np.pi,tope*np.pi,100)
                y2 = np.sin(x*2)
                plt.plot(x2, y2, color='blue',alpha=0.5)
                    
            elif(bites == "010"):

                x = np.linspace(base*np.pi,tope*np.pi,100)
                y = np.cos(x*2)
                plt.plot(x, y, color='green')

            elif(bites == "011"):

                x = np.linspace(base*np.pi,tope*np.pi,100)
                y = 2*np.cos(x*2)
                plt.plot(x, y, color='green', alpha=0.5)

            elif(bites == "110"):

                x = np.linspace(base*np.pi,tope*np.pi,100)
                y = -1*np.cos(x*2)
                plt.plot(x, y, color='red')

            elif(bites == "111"):

                x = np.linspace(base*np.pi,tope*np.pi,100)
                y = -2*np.cos(x*2)
                plt.plot(x, y, color='red', alpha=0.5)

            base = tope
            tope +=1 
            
                
        plt.axhline(y = 0, color="black")  
        plt.grid(axis='x', color='0.95')
        plt.title("4-PSK")
        # plt.title('ASK Modulación por dezplazamiento de amplitud')
        plt.show()  

    def trama_preparar_QAM(self, array_tramas):
        # le agregamos cero para que podamos hacer grupos de tres y usar el metodo para onda QAM
        largo_trama = len(array_tramas)*8
        ceros = ""

        while(True):

            if(largo_trama % 3 == 0):
                break
            else:
                ceros += "0"
                largo_trama += 1

        array_tramas[0] = ceros + array_tramas[0]

        trama_entera = ''.join(array_tramas)

        return trama_entera


if(__name__ == "__main__"):
    objeto = Ondas()
    objeto.ocho_QAM()
