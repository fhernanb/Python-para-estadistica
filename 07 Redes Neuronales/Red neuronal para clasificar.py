# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:54:20 2020

@author: fhern
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

# Crear el dataset
n = 500
p = 2

X, Y = make_circles(n_samples=n, factor=0.5, noise=0.05)

# Para ver los puntos
plt.scatter(X[:, 0], X[:, 1])

# Para diferenciar por colores
plt.scatter(X[Y == 0, 0], X[Y == 0, 1], c="skyblue")
plt.scatter(X[Y == 1, 0], X[Y == 1, 1], c="salmon")
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
    nn = []
    for l, layer in enumerate(topology[:-1]):
        nn.append(neural_layer(topology[l], topology[l+1], act_f))
    return nn

topology = [p, 4, 8, 16, 8, 4, 1]

create_nn(topology, sigm)

# Funcion para entrenar la red
def train():
        





