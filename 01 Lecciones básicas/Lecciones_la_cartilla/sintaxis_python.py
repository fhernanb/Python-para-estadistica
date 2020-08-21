# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:16:33 2020

@author: freddy
"""

"""
Este es un ejemplo de las lecciones de la cartilla
https://www.youtube.com/channel/UCobbRQK0QYlri_fo2Lalsxg
"""

# ===================================================================
# EJEMPLO CLASICO
# ===================================================================

print("Hola mundo")
print("Saludos desde Medellín")

# ===================================================================
# DEFINICION DE VARIABLES EN PYTHON
# ===================================================================

# Variable tipo string
saludo = "hola"
print(type(saludo))
type(saludo)
len(saludo)

objeto = "amigos"
objeto
type(objeto)
len(objeto)

# Variable tipo entero
num_camisas = 18
num_camisas
type(num_camisas)

num_pantalones = 2
num_pantalones
type(num_pantalones)

# Variable tipo float
valor_pi = 3.1416 
type(valor_pi)

# Variables tipo boolean
es_mujer = False
es_colombiano = True

# multiplicacion de enteros y float
num_ropa = num_camisas * num_pantalones
num_ropa
type(num_ropa)

aux = valor_pi * num_camisas
aux
type(aux)

# suma de strings
print(saludo + " " + objeto)
print(saludo + " " + objeto + " mis camisas son " + str(num_camisas))






