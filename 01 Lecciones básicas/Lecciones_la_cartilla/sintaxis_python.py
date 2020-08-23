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
# OPERADORES EN PYTHON
# ===================================================================

# Para consultar la lista de operadores revisar
# https://www.w3schools.com/python/python_operators.asp

# Operadores aritmeticos
x = 10
x / 3
x // 3
x % 3
x ** 2

# Operadores de asignacion
y = "la cartilla"

x += 5 # significa x = x + 5
x

x -= 10
x

x /= x
x

y += " python3"
y

# Operadores de comparacion
y == y
x == y
x ==  1

x != y
x != 1

True != False

10.5638 < 11.2324
len(y) > x

# Operadores logicos
x < 5 and x < 10
x < 5 or x < 4
not(x < 5 and x < 10)

# Operadores de identidad
x is x
y is x
y is not x

# Operadores de pertenencia
lista1 = [1, 2, 3, 4, 5]

3 in lista1
10 not in lista1
4 not in lista1
"la" in y

# Bitwise Operators
(x < 5) & (x < 10)


