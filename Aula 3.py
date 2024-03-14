#Faça um programa que leia raiz A², B², C² e calcule:

import math
print("=================================")
A = float(input("Digite o valor de A: "))
print("=================================")
B = float(input("Digiteo valor de B: "))
print("=================================")
C = float(input("Digite o valor de C: "))
resultado = math.sqrt (A**2 + B**2 + C**2)
print("=================================")
print("O resultado do calculo é: ",round(resultado,2))

#Leia do usuario A e B e cacule resultado = raiz seno A + seno B e calcule:

import math

print("=================================")
A = float (input("Digite o valor de A: "))
print("=================================")
B = float (input("Digite o valor de B: "))

resultado = math.sqrt(math.sin(A) + math.sin(B))
print("=================================")
print("O resultado desta equação é: ", resultado)

#Leia A, B e C. Calcule resultado √A+√B+√C

import math

print("=================================")
A = float(input("Digite o valor de A: "))
print("=================================")
B = float(input("Digiteo valor de B: "))
print("=================================")
C = float(input("Digite o valor de C: "))

resultado = math.sqrt (A) + math.sqrt (B) + math.sqrt (C)

print("O resultado da equação é: ", round(resultado, 2))

