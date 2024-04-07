import numpy as np

# Crear una lista / arreglo / vector / array
lista = np.array([1,2,3,4,5]) # One direction, unidimensional
# print(lista)

listaBidi = np.array(
  [
    [1,2,3,4],
    [5,6,7,8]
  ]) # Two directions, bidimensional


# np.ones((filas, columnas, dimensiones),tipoDato)
# uint8 => unsigned int 
# [filas,columnas,dimensiones]
img = np.ones( (5,5,3), np.uint8)
print(img[:,:,0])