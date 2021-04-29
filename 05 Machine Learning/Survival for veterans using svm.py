# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:28:26 2020

@author: fhern
"""

"""
Este ejemplo fue tomado de 
https://notebook.community/sebp/scikit-survival/examples/survival-svm
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas
import seaborn as sns
from sklearn.model_selection import ShuffleSplit, GridSearchCV

from sksurv.datasets import load_veterans_lung_cancer
from sksurv.column import encode_categorical
from sksurv.metrics import concordance_index_censored
from sksurv.svm import FastSurvivalSVM

data_x, y = load_veterans_lung_cancer()

print("\n")
print("La matriz con las covariables")
print(data_x.head())

print("\n")
print("Las primeras 5 observaciones de y")
print(y[0:4])

# Para convertir la matriz con las covariables
x = encode_categorical(data_x)

print("\n")
print("Para ver el inicio de la matriz x")
print(x.head())

# Para saber el numero de observaciones censuradas
n_censored = y.shape[0] - y["Status"].sum()

print("\n")
print("%.1f%% of records are censored" % (n_censored / y.shape[0] * 100))

# Dibujando
plt.figure(figsize=(9, 6))
val, bins, patches = plt.hist((y["Survival_in_days"][y["Status"]],
                               y["Survival_in_days"][~y["Status"]]),
                              bins=30, stacked=True)
plt.legend(patches, ["Time of Death", "Time of Censoring"])

# First, we need to create an initial model with default parameters 
# that is subsequently used in the grid search.

estimator = FastSurvivalSVM(optimizer="rbtree", 
                            max_iter=1000, 
                            tol=1e-6, 
                            random_state=0)

# Creando la metrica
def score_survival_model(model, X, y):
    prediction = model.predict(X)
    result = concordance_index_censored(y['Status'], 
                                        y['Survival_in_days'], 
                                        prediction)
    return result[0]


param_grid = {'alpha': 2. ** np.arange(-12, 13, 2)}
cv = ShuffleSplit(n_splits=200, test_size=0.5, random_state=0)
gcv = GridSearchCV(estimator, param_grid, scoring=score_survival_model,
                   n_jobs=4, iid=False, refit=False, cv=cv)

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
gcv = gcv.fit(x, y)

# Resultados de la busqueda del valor de alpha
gcv.best_score_, gcv.best_params_

# Creando el modelo nuevamente
model = FastSurvivalSVM(alpha=0.00390625)
model_fitted = model.fit(x, y)
model_fitted.score(x, y)
model_fitted.predict(x)

# Para hacer la prediccion
y_hat = model_fitted.predict(x)
y_hat

