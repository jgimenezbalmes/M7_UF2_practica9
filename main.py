import numpy as np
import exercici1 as ex1
import exercici4_Joan_Gimenez as ex4
import exercici2 as createArray
import exercici2 as createArray2
import exercici2 as createArray3
#Joan
#Exercici 1
a = ex1.ex1()
print('Matriu 50x50 amb una diagonal que va de 0 a 49')
print(a)
print ("Dimensio de la matriu (numero de eixos)")
print (a.ndim)
print ("Tamany de la matriu (llargada de cada eix)")
print (a.shape)
print ("Número total d'elements (quants valors hi ha a la matriu)")
print (a.size)
print ("Tipus d'elements interns (si son integer, double,...)")
print (a.dtype)

#Jonathan
#Exercici 2
b = createArray.createArray()
print("Array Funcion 1")
print(b)
c = createArray.createArray2()
print("Array Funcion 2")
print(c)
d = createArray.createArray3()
print("Array Funcion 3")
print(d)
