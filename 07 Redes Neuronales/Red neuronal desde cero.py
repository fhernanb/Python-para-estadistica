# Ejemplo tomado de 
# https://medium.com/@jcrispis56/una-introducci%C3%B3n-completa-a-redes-neuronales-con-python-y-tensorflow-2-0-b7f20bcfebc5#:~:text=Una%20Introducci%C3%B3n%20Completa%20A%20Redes%20Neuronales%20Con%20Python,se%20llaman%20variables%20dependientes%20...%20Mas%20cosas...%20
# https://iamtrask.github.io/2015/07/12/basic-python-network/

import numpy as np

# Funcion logit inversa o sigmoide
def nonlin(x, deriv=False):
	if(deriv==True):
	    return x*(1-x)
	return 1/(1+np.exp(-x))

# A continuacion los datos
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])

# Este es el vector de respuestas
y = np.array([[0],
	          [1],
	          [1],
	          [0]])

# Se fija la semilla
np.random.seed(1)

# Para crear los valores de inicio que van a estar entre -1 y 1
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

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