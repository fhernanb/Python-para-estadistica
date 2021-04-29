# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:01:05 2020

@author: fhern

Los ejemplos mostrados aquí corresponden al libro Python for Data Analysis
"""

import numpy as np

# Creando un array a partir de una lista
data1 = [6, 7.5, 8, 0, 1]
print(data1)

arr1 = np.array(data1)
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.dtype)

# Creando un array a partir de una lista
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(data2)

arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.dtype)

# Array a partir de una lista con elementos de diferente longitud
lista1 = [[1, 2, 3], [4, 5], [6.86954]]
print(lista1)

arr3 = np.array(lista1)
print(arr3)
print(arr3.ndim)
print(arr3.shape)
print(arr3.dtype)

# Creando arreglos de ceros, unos y vacíos
np.zeros(5)
np.zeros((6, 6))
np.zeros((3, 2, 4))
np.zeros((2, 3, 2, 5))

np.ones(10)
np.ones((9, 9))

np.empty(6)
np.empty((3, 3))

# Para crear arreglos usando arange o range
# la función arange 
np.arange(8)
np.array(range(8))

