import numpy as np
import math as m
import matplotlib.pyplot as plt
from logica.Palabras_binarias import PalabrasBinarias


class Ondas(PalabrasBinarias):

    def Graficar_onda(self, direcion_ondas, amplitud_onda1, frecuencia_onda1, amplitud_onda2, frecuencia_onda2, cambio_fase, oracion, titulo):

        base = 0
        tope = 1
        color_1 = 0.5
        color_0 = 0.5
        array = self.Convertir_binario(oracion)
        direccion = direcion_ondas

        for trama in array:
            for bit in trama:

                if(bit == "1"):

                    if(cambio_fase):
                        direccion = -1

                    x = np.linspace(base*np.pi, tope*np.pi, 100)
                    y = direccion*amplitud_onda1*np.sin(x*frecuencia_onda1)
                    plt.plot(x, y, color='black', alpha=color_1)

                    color_1 = 1 if color_1 == 0.5 else 0.5

                else:
                    if(cambio_fase):
                        direccion = 1

                    x2 = np.linspace(base*np.pi, tope*np.pi, 100)
                    y2 = direccion*amplitud_onda2*np.sin(x2*frecuencia_onda2)
                    plt.plot(x2, y2, color='green', alpha=color_0)
                    color_0 = 1 if color_0 == 0.5 else 0.5

                base = tope
                tope += 1

        self.graficar(titulo=titulo,array_binario=array)

    def ASK(self,frase):
        self.Graficar_onda(direcion_ondas=-1,
                           amplitud_onda1=4,
                           frecuencia_onda1=2,  # la onda 1 se refiere a la onda de 1 y la onda 2 es la onda del cero
                           amplitud_onda2=1,
                           frecuencia_onda2=2,
                           cambio_fase=False,
                           oracion=frase,
                           titulo='ASK Modulación por dezplazamiento de amplitud'
                           )

    def FSK(self,frase):
        self.Graficar_onda(direcion_ondas=-1,
                           amplitud_onda1=2,
                           frecuencia_onda1=6,
                           amplitud_onda2=2,
                           frecuencia_onda2=2,
                           cambio_fase=False,
                           oracion=frase,
                           titulo='FSK Modulación por dezplazamiento de frecuencia'
                           )

    def PSK(self, frase):

        self.Graficar_onda(direcion_ondas=1,
                           amplitud_onda1=1,
                           frecuencia_onda1=2,
                           amplitud_onda2=1,
                           frecuencia_onda2=2,
                           cambio_fase=True,
                           oracion=frase,
                           titulo='PSK Modulación por dezplazamiento de fase'
                           )

    def cuatro_PSK(self,oracion):
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

        self.graficar("4-PSK",array)
 

    def ocho_QAM(self,oracion):

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
                y2 = np.sin(x2*2)
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
            
        self.graficar("8-QAM",trama_completa)


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

    def unipolar(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8
        x = [i for i in range(largo+1)]
        y = []
        for trama in array:
            for bit in trama:

                if(bit == "1"):
                   
                   y.append(20)

                else:
                
                    y.append(0)
        y.append(0)

        self.graficar("Unipolar",array,x,y,"post")
    

    def NRZ_L(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8
        x = [i for i in range(largo+1)]
        y = []
        for trama in array:
            for bit in trama:

                if(bit == "1"):
                   
                   y.append(-5)

                else:
                
                    y.append(5)
        y.append(0)

        self.graficar("NRZ-L",array,x,y,"post")


    def NRZ_I(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8
        x = [i for i in range(largo+1)]
        y = []
        direccion = 5
        for trama in array:
            for bit in trama:

                if(array.index(trama) == 0 and bit == trama[:2] and bit == "1"):
                    direccion = -5
                elif(array.index(trama) == 0 and bit == trama[:2] and bit == "0"):
                    direccion = 5   
                else:
                    if(bit == "1"):
                        direccion = -1*direccion
                
                    
                y.append(direccion)

        y.append(0)
        self.graficar("NRZ-I",array,x,y,"post")
      
    def RZ(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8
        acumulador = -0.5
        x = []
        for i in range(-1,largo*2):
            acumulador += 0.5
            x.append(acumulador)

        y = [0]
        for trama in array:
            for bit in trama:

                if(bit == "1"):
                   
                   y.append(5)
                   y.append(0)

                else:
                
                    y.append(-5)
                    y.append(0)
        self.graficar("RZ",array,x,y,"pre")
        
    def Manchester(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8
        acumulador = -0.5
        x = []
        for i in range(-1,largo*2+1):
            acumulador += 0.5
            x.append(acumulador)

        y = [0]
        for trama in array:
            for bit in trama:

                if(bit == "1"):
                   
                   y.append(-10)
                   y.append(10)

                else:
                
                    y.append(10)
                    y.append(-10)

        y.append(0)
        self.graficar("Manchester",array,x,y,"pre")
        

    def Manchester_diff(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8
        acumulador = -0.5
        x = []
        for i in range(-1,largo*2+1):
            acumulador += 0.5
            x.append(acumulador)

        y = [0]
        primera_m = 0
        segunda_m = 0
        for trama in array:
            for bit in trama:

                if(len(y) == 1):

                    if(bit == "1"):
                        primera_m = 10
                        segunda_m = -10
                    
                    elif(bit == "0"):
                        primera_m = -10
                        segunda_m = 10
                else:

                    if(bit == "1"):
                    
                        aux = primera_m
                        primera_m = segunda_m
                        segunda_m = aux

                    
                y.append(primera_m)
                y.append(segunda_m)

        y.append(0)
        self.graficar("Manchester dif",array,x,y,"pre")

    def AMI(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8
        x = [i for i in range(largo+1)]
        y = []
        numero = 10
        for trama in array:
            for bit in trama:

                if(bit == "1"):

                   y.append(numero)

                   numero = -1*numero

                else:
                
                    y.append(0)
        y.append(0)
        self.graficar("AMI",array,x,y,"post")
      

    def B8ZS(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8
        x = [i for i in range(largo+1)]
        y = []
        numero = 10
        ceros = 0
        violacion = False
        signos = 0
        trama = "".join(array)

        for bit in range(len(trama)):

            if(ceros == 3 and trama[bit] == "0" and trama[bit+1:bit+5] == "0000"):

                violacion = True
                y.append(-1*numero)
                signos +=1
            elif(violacion and signos == 1):
                y.append(numero)
                signos +=1

            elif(signos==2 and violacion):
                y.append(0)
                signos += 1
            elif(signos==3 and violacion):
                y.append(numero)
                signos += 1
            elif(signos==4 and violacion):
                y.append(-1*numero)
                signos = 0
                ceros = 0
                violacion = False
            else:
                if(trama[bit] == "1"):

                    y.append(numero)
                    numero = -1*numero
                    ceros = 0

                else:
                    ceros += 1
                    y.append(0)

        y.append(0) 

        self.graficar("B8ZS",array,x,y,metodo="post")
       
    def HDB3(self,oracion):

        array = self.Convertir_binario(oracion)
        largo = len(array)*8 
        x = [i for i in range(largo+1)]
        y = []
        numero = 10
        unos = 0
        trama = "".join(array)
        bit = 0
        while(bit < len(trama)):

            if(trama[bit:bit+4] == "0000"):

                if(unos%2 == 0):

                    if(numero < 0):

                        y.append(-10)
                        y.append(0)
                        y.append(0)
                        y.append(-10)

                        bit += 4
                    else:
                        y.append(10)
                        y.append(0)
                        y.append(0)
                        y.append(10)

                        bit += 4
                else:

                    if(numero < 0):

                        y.append(0)
                        y.append(0)
                        y.append(0)
                        y.append(10)

                        bit += 4
                    else:
                        y.append(0)
                        y.append(0)
                        y.append(0)
                        y.append(-10)

                        bit += 4
            else:

                if(trama[bit] == "1"):

                    y.append(numero)
                    numero = -1*numero
                    unos += 1

                else:

                    y.append(0)

                bit += 1 

        y.append(0) 

        self.graficar("HDB3",trama,x,y,metodo="post")

    def Analogica_digital(self,numeros):

        array = []
        for entero in numeros:
            resultado = bin(entero)[2:]
            if(resultado[:1] == "b"):
                resultado = "1"+(7-len(resultado[1:]))*"0" + resultado[1:]
            else:
                resultado = (8-len(resultado))*"0" + resultado
            array.append(resultado)

        x = [i for i in range((len(array)*8)+1)]
        y = []
        for trama in array:
            for bit in trama:

                if(bit == "1"):
                   
                   y.append(20)

                else:
                
                    y.append(0)
        y.append(0)

        self.graficar("Analógica a digital",array,x,y,metodo="post")
        
    def graficar(self,titulo,array_binario,x=[],y=[],metodo="post"):

        cadena_binaria = "".join(array_binario)
        if(len(x)>0 and len(y)>0):

            plt.step(x, y, where=metodo, label=metodo)
       
       
        plt.axhline(y=0, color="grey", alpha=0.5)
        plt.axvline(x=0, color="black")
        plt.grid(color='grey',alpha=0.2, linestyle='-', axis='x')
        plt.title(titulo)
        font2 = {'family':'serif','color':'darkred','size':15}
        plt.xlabel(cadena_binaria,fontdict = font2)
        plt.show()

