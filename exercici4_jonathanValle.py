# Importamos numpy
import numpy as np

# Ejercicio 4
def ex4_jonathan_valle():
    ## Generar numeros de 0 a 80 con una dimension de 4x3
    a = np.random.randint(81, size=(4,3))
    # Cambiar la matriz de 4x3 por 3x4
    b = a.reshape(3,4)
    # Eliminar la ultima columna de la matriz (axis=1) para indicar que es columna
    c = np.delete(b, 3, axis=1)
    # Obtenemos la ultima fila
    i = c[-1,-1]
    # Insertamos la fila obtenida a la ultima columna
    fila = np.insert(c, 3, i, axis=1)
    # Al retornar varios resultados, lo ponemos dentro de un parantesis y con una coma
    return (a, b, c, fila)
ex4_jonathan_valle()
