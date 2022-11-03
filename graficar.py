import numpy as np
import math as m
import matplotlib.pyplot as plt
from Palabras_binarias import PalabrasBinarias 



objeto = PalabrasBinarias() 
array = objeto.Convertir_binario("ESTEFANIA LLAMAS DE LA CRUZ")

cantidad = lambda array: len(array)*8 

numero_limite = cantidad(array)


# Some example data to display
x = np.linspace(0,numero_limite*np.pi,numero_limite*100)#particiones
y = []
inicio = 0
fin = 100


for trama in array:
    for bit in trama:

        if(bit == "1"):
            pedazo_x = x[inicio:fin]
            resultado_sin = 10*np.sin(pedazo_x)
            y += resultado_sin.tolist()
           
        else:
            pedazo_x = x[inicio:fin]
            resultado_sin = np.sin(pedazo_x)
            y += resultado_sin.tolist()
           

        inicio = fin
        fin +=100
        
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('ASK Modulación por dezplazamiento de amplitud') 
plt.axhline(y = 0, color="black")  

""" fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A single plot')
plt.axhline(y = 0, color="black")  
"""
"""
x = np.linspace(0,80)
linea_bit1 = np.linspace(0,10)
linea_bit2 = np.linspace(10,20)
onda_abajo = -(np.sin(linea_bit1))
onda_arriba = np.sin(linea_bit2)
y = np.concatenate((onda_abajo,onda_arriba),axis=0)

#plt.step(x, y, label='pre (default)')
plt.plot(x, y, color='grey', alpha=0.3)
# line colour is red
plt.axhline(y = 0, color="black")    
    
# adding axis labels    
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.step(x, y + 1, where='mid', label='mid')
plt.plot(x, y + 1, 'o--', color='grey', alpha=0.3)

plt.step(x, y, where='post', label='post')
plt.plot(x, y, 'o--', color='grey', alpha=0.3) """

plt.grid(axis='x', color='0.95')
plt.show() 
