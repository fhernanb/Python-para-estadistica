# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:43:09 2020

@author: fhern
"""

import numpy as np

# Funcion logit inversa o sigmoide
def nonlin(x, deriv=False):
	if(deriv==True):
	    return x*(1-x)
	return 1/(1+np.exp(-x))

# A continuacion los datos
X = np.array([[1.2, 3.8],
              [-1.7, 4.9],
              [2.1, -1.4]])

# Este es el vector de respuestas
y = np.array([[6.2],
	          [25.5],
	          [-4.5]])
    
# Se fija la semilla
np.random.seed(1)

# Para crear los valores de inicio que van a estar entre -1 y 1
syn0 = 2 * np.random.random((2, 3)) - 1
syn1 = 2 * np.random.random((3, 1)) - 1

for j in range(6000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    l2_error = y - l2
    l2_delta = l2_error * nonlin(l2, deriv=True)

    l1_error = l2_delta.dot(syn1.T)
    l1_error = np.dot(l2_delta, syn1.T)
    
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print("El resultado es: \n")
print(l2)

