import numpy as np
#Creamos nuestra funcion
def function4():
    #Creamos nuestro matriz de 4 x 3 - Aleatorio (0 - 80)
    array = np.random.randint(80, size=(4, 3))
    #Modificamos la lista anterior por 3 x 4
    array = np.resize(list,(3,4))
    array = array.T
    return array


