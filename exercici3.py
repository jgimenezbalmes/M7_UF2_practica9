import numpy as np
#Funcion Numero Aleatorios
def aleatorio(a):
    m = np.random.randint(0,101, size=a)
    return m
#Funcion del Valor Maximo
def valorMaximo(m):
    max = np.amax(m, axis=1)
    return max

#Funcion de Valor minimo
def valorMinimo(m):
    min = np.amin(m, axis=1)
    return min






