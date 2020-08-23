# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:54:20 2020

@author: fhern
"""

"""
Este ejemplo está basado en el video
https://youtu.be/W8AeOXa_FqU
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

# Crear el dataset
n = 500
p = 2

X, Y = make_circles(n_samples=n, factor=0.5, noise=0.05)

Y = Y[:, np.newaxis]

# Para ver los puntos
plt.scatter(X[:, 0], X[:, 1])

# Para diferenciar por colores
plt.scatter(X[Y[:, 0] == 0, 0], X[Y[:, 0] == 0, 1], c="skyblue")
plt.scatter(X[Y[:, 0] == 1, 0], X[Y[:, 0] == 1, 1], c="salmon")
plt.axis("equal")
plt.show()

# Definir una clase de la capa de la red
class neural_layer():
    def __init__(self, n_conn, n_neur, act_f):
        self.act_f = act_f
        self.b = np.random.rand(1, n_neur)      * 2 - 1
        self.W = np.random.rand(n_conn, n_neur) * 2 - 1

# Definir las funciones de activacion
sigm = (lambda x: 1 / (1 + np.e ** (-x)),
        lambda x: x * (1 - x))

relu = lambda x: np.maximum(0, x)

# Para ver la funcion sigmoide
_x = np.linspace(-5, 5, 100)
plt.plot(_x, sigm[0](_x), c="red")
plt.plot(_x, sigm[1](_x), c="blue")
plt.show()

# Para ver la funcion relu
_x = np.linspace(-5, 5, 100)
plt.plot(_x, relu(_x), c="orange")
plt.show()

# Creando la red
def create_nn(topology, act_f):
    nn = [] # vector que contiene la red
    for l, layer in enumerate(topology[:-1]):
        nn.append(neural_layer(topology[l], topology[l+1], act_f))
    return nn

# Esto sirve para crear las capas y las neuronas dentro de cada capa
topology = [p, 4, 8, 16, 8, 4, 1]

# Creamos la red
neural_net = create_nn(topology, sigm)

# Funcion de costos
l2_cost = (lambda Yp, Yr: np.mean((Yp - Yr) ** 2),
           lambda Yp, Yr: (Yp - Yr))

# Funcion para entrenar la red
def train(neural_net, X, Y, l2_cost, lr=0.5, Train=True):
    
    out = [(None, X)]
    
    # Forward pass
    for l, layer in enumerate(neural_net):
        
        z = out[-1][1] @ neural_net[l].W + neural_net[l].b
        a = neural_net[l].act_f[0](z)
        out.append((z, a))
        
    if train:
        
        # Backward pass
        deltas = []
        for l in reversed(range(0, len(neural_net))):
            
            z = out[l+1][0]
            a = out[l+1][1]
           
            if l == len(neural_net) - 1:
                deltas.insert(0, l2_cost[1](a, Y) * neural_net[l].act_f[1](a))
            else:
                deltas.insert(0, deltas[0] @ _W.T * neural_net[l].act_f[1](a))
                
            _W = neural_net[l].W
            
            # Gradient descent
            neural_net[l].b = neural_net[l].b - np.mean(deltas[0], axis=0, keepdims=True) * lr
            neural_net[l].W = neural_net[l].W - out[l][1].T @ deltas[0] * lr
            
        return(out[-1][1])
        
    
train(neural_net, X, Y, l2_cost, 0.5)

