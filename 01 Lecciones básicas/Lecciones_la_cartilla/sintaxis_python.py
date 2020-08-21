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

# ===================================================================
# OPERACIONES
# ===================================================================

# multiplicacion
num_ropa = num_camisas * num_pantalones
num_ropa
type(num_ropa)

aux = valor_pi * num_camisas
aux
type(aux)

print(5 * saludo)

# suma de strings
print(saludo + " " + objeto)
print(saludo + " " + objeto + " mis camisas son " + str(num_camisas))

# potencias
num_camisas ** 2

# divisiones
num_camisas / num_pantalones
9 // 2 # para obtener parte entera

# ===================================================================
# DEFINICION USANDO math
# ===================================================================
import math

math.factorial(5)
math.floor(5.3)
math.ceil(5.3)
math.sin(math.pi)
math.cos(math.pi)
math.tan(math.pi)
math.log(100, 10)
math.pow(2, 3)
math.degrees(math.pi)
math.radians(180)
math.exp(1)
math.gcd(20, 15)
math.pi
math.tau

round(3.1416, 1)

# ===================================================================
# BUILT IN FUNCTION
# ===================================================================
# Se pueden consultar en
# https://docs.python.org/3/library/functions.html

abs(-3.14)
dir()

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))

x = 1
eval('x+1')

# ===================================================================
# IMPORTAR LIBRERIA O MODULO O PAQUETE
# ===================================================================




