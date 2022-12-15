# Importamos numpy
import numpy as np

# Funcion 1
def createArray():
    # Creamos un array con dichos varoles y lo retornamos
    a = np.array([88, 23, 39, 41])
    return a

# Funcion 2
def createArray2():
    # Creamos un array con 2 arrays flotantes y lo retornamos
    b = np.array([[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]], np.float32)
    return b

# Funcion 3
def createArray3():
    # Crear un array con una dimension y lo retornamos
    c = np.array([[12],[4],[9],[8]])
    return c