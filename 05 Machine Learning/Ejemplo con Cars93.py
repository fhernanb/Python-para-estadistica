# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:32:23 2020

@author: fhern
"""

# Librerías a usar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leyendo la base de datos Cars93 del paquete MASS de R
file = 'https://raw.githubusercontent.com/fhernanb/datos/master/Cars93_MASS.txt'
dt = pd.read_csv(file, sep="\t")
dt.head()

# Creando las matrices x e y con la información
X = dt[["EngineSize", "Weight", "MPG.city"]]
y = dt["Price"]

# Librerías para ajustar el modelo de interés
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings("ignore")

# Vamos a mostrar como cambian los coeficientes para diferentes valores de 
# del parámetro alpha (o también conocido como lambda)

# Creando los diferentes valores de alpha
n_alphas = 20
alphas = np.logspace(0, 7, n_alphas)
alphas

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=True)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)
    
# Display results
ax = plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim()[::-1])  # reverse axis
plt.xlabel('alpha')
plt.ylabel('Coefficients')
plt.title('Ridge coefficients as a function of the regularization')
plt.axis('tight')
plt.show()

# Buscando el valor de alpha que minimiza la metrica -------------------------
# que puede ser: r2, neg_mean_squared_error, max_error entre otras

parameters = {'alpha': np.concatenate((np.arange(0.1, 2, 0.1), 
                                       np.arange(2, 5, 0.5), 
                                       np.arange(5, 25, 1)))}
print(parameters)

ridge = linear_model.Ridge()
gridridge = GridSearchCV(ridge, parameters, scoring ='neg_mean_squared_error')
gridridge.fit(X, y)

print("ridge best parameters:", gridridge.best_params_)
print("ridge score:", gridridge.score(X, y))
print("ridge r2:", r2_score(y, gridridge.predict(X)))
print("ridge MSE:", mean_squared_error(y, gridridge.predict(X)))
print("ridge best estimator coef:", gridridge.best_estimator_.coef_)

# Creando el modelo con el alpha óptimo --------------------------------------
ridge = linear_model.Ridge(alpha=0.5, fit_intercept=True)

# Creando el modelo
ridge.fit(X, y)

# Print scores, MSE, r2 and coefficients
print("ridge score:", ridge.score(X, y))
print("ridge MSE:", mean_squared_error(y, ridge.predict(X)))
print("ridge r2:", r2_score(y, ridge.predict(X)))
print("ridge coef:", ridge.coef_)

# Voy a estimar y usando valores caprichosos de las x's ----------------------
new_X = [[2, 3100, 25], [4, 3500, 21]]
print(new_X)
prediccion = ridge.predict(new_X)
print(prediccion)
