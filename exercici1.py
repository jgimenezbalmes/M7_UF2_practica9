import numpy as np

def ex1():
    #Fem una matriu de zeros de 50x50
    a = np.zeros((50,50))
    #Fem una matriu unidimensional que va de 0 a 49
    arr = np.array(range(50), dtype='int32')
    #Fiquem la matriu unidimensional a la diagonal de la matriu 50x50
    a = np.diag(arr)
    #Guardem la matriu resultant a un arxiu npy
    np.save('exercici1.npy', a)
    #Fem return de a
    return a
