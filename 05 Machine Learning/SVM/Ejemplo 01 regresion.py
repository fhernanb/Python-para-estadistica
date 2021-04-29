# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:50:59 2020

@author: fhern
"""

# Librerías a usar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leyendo la base de datos Cars93 del paquete MASS de R
file = 'https://raw.githubusercontent.com/fhernanb/datos/master/Ejemplo_01_svm.txt'
dt = pd.read_csv(file, sep="\t")
dt.head()

# Creando las matrices x e y con la información
X = dt[["x"]]
y = dt["y"]

# Librerías para ajustar el modelo de interés
from sklearn.svm import SVR

# Define and Fit regression models
svr_lin = SVR(kernel='linear', C=1, epsilon=0.1, gamma='auto')
svr_pol = SVR(kernel='poly', C=1, epsilon=0.1, gamma=1, degree=3, coef0=0)
svr_rbf = SVR(kernel='rbf', C=1, epsilon=0.1, gamma=1)

svr_lin.fit(X, y)
svr_pol.fit(X, y)
svr_rbf.fit(X, y)

# Print scores, MSE, and coefficients
print("R^2 prediction:", svr_lin.score(X, y))
print("R^2 prediction:", svr_pol.score(X, y))
print("R^2 prediction:", svr_rbf.score(X, y))

# Calculando las predicciones
y_hat_lin = svr_lin.predict(X)
y_hat_pol = svr_pol.predict(X)
y_hat_rbf = svr_rbf.predict(X)

# Calculando MSE
np.mean((y_hat_lin - y)**2)
np.mean((y_hat_pol - y)**2)
np.mean((y_hat_rbf - y)**2)

# Calculando las correlaciones
np.corrcoef(y_hat_lin, y)
np.corrcoef(y_hat_pol, y)
np.corrcoef(y_hat_rbf, y)

# Voy a estimar y usando valores caprichosos de las x's
new_X = [[0], [2], [4]]
print(new_X)
prediccion = svr_lin.predict(new_X)
print(prediccion)


