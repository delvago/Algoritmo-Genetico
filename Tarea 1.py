import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt

#Función que se busca optimizar empleada para el fitness.
#Parametros de entrada:
#x: Variable 1.
#y: Variable 2.
#Parametros de salida:
#f: Resultado al evaluar la función.
def funcionEvaluada(x,y):
    f = -(y+47)*np.sin(np.sqrt(np.abs(y+(x/2)+47)))-x*np.sin(np.sqrt(np.abs(x-(y+47))))
    return f


#Transforma un número entero positivo o negativo a binario de 11 bits 
def toBinary(num):
    if num >= 0:
        return bin(num)[2:].zfill(10) # convierte el número a binario y agrega ceros a la izquierda para que tenga 10 bits
    else:
        # convierte el número a su complemento a dos y lo agrega a la cadena de bits
        return bin(1024 + num)[2:]

#Transforma un número binario positivo o negativo de 11 bits a entero
def toInt(bits):
    if bits[0] == '0':
        return int(bits, 2) # convierte la cadena de bits a un número entero en base 2
    else:
        # calcula el complemento a dos del número y lo convierte a decimal
        complement = int(''.join(['1' if bit == '0' else '0' for bit in bits]), 2)
        return -(complement + 1)

#Esta función genera la población.
#Parametros de entrada:
#chromosomes: Es la población de cromosomas a generar.
#genes: Es el número de genes de cada cromosoma.
#lowerlimit: Límite inferior del valor que pueden tomar los genes.
#upperlimit: Límite superior del valor que pueden tomar los genes.
#Parametros de salida:
#matriz: Matriz poblacional.
def populationGeneration(chromosomes, genes, lowerlimit, upperlimit):
    matriz = np.random.randint(lowerlimit, upperlimit+1, size=(chromosomes, genes))
    return matriz    

#Función para codificar
def codificacion(matriz:np.ndarray):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            matriz[i][j]=toBinary(matriz[i][j])
    return matriz

def decodificacion(matriz:np.ndarray):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            matriz[i][j]=toInt(f'{matriz[i][j]}')
    return matriz

population = 20

binario=toBinary(-512)
print(binario)
entero=toInt(binario)
print(entero)

# matriz=populationGeneration(20,2,-512,512)
# print(matriz)

# binario=codificacion(matriz)
# print(binario)

# contra=decodificacion(binario)
# print(binario)

