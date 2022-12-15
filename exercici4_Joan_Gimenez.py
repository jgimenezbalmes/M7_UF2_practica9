import numpy as np

def ex4_Joan_Gimenez():
    #Genera un array 4x3 de valors aleatoris entre 0 i 80
    b = np.random.randint(0, 81, size=(3, 4))
    #Modifiquem la matriu a 3x4 i l'ultima fila passa a ser columna
    c = b.reshape(4,3)
    fila = c[3, :]
    fila= fila.reshape(3,1)
    c = np.delete(c, 2, axis=0)
    c = np.append(c, fila, axis=1)
    d = c.copy()
    d[:,3]=d[0,3]

    return b, c, d