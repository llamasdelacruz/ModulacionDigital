
class PalabrasBinarias():

    def bit_paridad(self,cadena_bits):
        #agrega el bit de paridad a unna cadena de 7 bits
        #regresa una cadena
        contador = 0
        for uno in cadena_bits:
            if(uno == "1"):
                contador += 1
        
        if(contador%2 == 0):
            cadena_bits = "0"+cadena_bits
        else:
            cadena_bits = "1"+cadena_bits

        return cadena_bits
            
    def Convertir_binario(self,frase):
        #convierte palabras a codigo bnario de 7 bits y agrega el bit de paridad para que sean 8
        #devuelve una lista con los bits en forma de cadena
        l,m=[],[]
        for i in frase:

            l.append(ord(i))

        for i in l:

            cadena_bits = bin(i)[2:]

            if(len(cadena_bits) < 7):

                cantidad_faltante = 7-len(cadena_bits)
                cadena_bits = ("0"*cantidad_faltante) + cadena_bits

            m.append(self.bit_paridad(cadena_bits))
        return m

