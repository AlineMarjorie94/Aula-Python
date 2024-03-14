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

#Faça um programa que leia do usuario: - População atual - Taxa de crescimento - anos
#Calcular populaçãofutura = populaçãoatual*(1+taxadecrescimento)^anos

import math
print("=================================")
populacaoatual = int(input("Digite o valor da população atual: "))
print("=================================")
crescimento = int(input("Digite a porcentagem de crescimento anual(5 para 5%): "))
print("=================================")
anos = int(input("Digite quantos anos: "))

resultado = populacaoatual * math.pow (1 + (crescimento/100), anos)
print("=================================")
print("A população futura será aprximadamente: ", resultado)

print("O resultado da equação é: ", round(resultado, 2))

#Faça um programa que leia x1, x2, y1, y2 e calcule a distâcia euclediana entre os pontos A(x1,x2) B(y1,y2)
#distancia = √(x2-x1)² + (y2-y1)²
import math
print("=================================")
x1 = float(input("Digite o valor de x1: "))
print("=================================")
x2 = float(input("Digite o valor de x2: "))
print("=================================")
y1 = float(input("Digite o valor de y1: "))
print("=================================")
y2 = float(input("Digite o valor de y2: "))

resultado = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1,2))

print("A distancia euclediana é de:",round(resultado, 2))
#Calculo da diagonal de um triangulo: - Leia largura - Leia o comprimento
#Calcule: diagonal = √largura²+comprimento²

import math

print("=================================")
largura = float(input("Digite o valor da largura: "))
print("=================================")
comprimento = float(input("Digite o valor da altura: "))
diagonal = math.sqrt(math.pow(largura, 2) + math.pow(comprimento,2))
print("=================================")
print("O valor da diagonal é: ",diagonal)

#Faça um programa que leia A,B,C,D e calcule
# x=a²-√b² y=c²+√d² r=√(x+y)²

import math

print("=================================")
A = float(input("Digite o valor de A: "))
print("=================================")
B = float(input("Digiteo valor de B: "))
print("=================================")
C = float(input("Digite o valor de C: "))
print("=================================")
D = float(input("Digite o valor de D: "))

x = A**2 - math.sqrt(B**2)
y = C**2 + math.sqrt(D**2)
r = math.sqrt(math.pow(x+y, 2))
print("=================================")
print("O Resultado de x=a²-√b² é: ",x)
print("O Resultado de y=c²+√d² é: ",y)
print("O Resultado de r=√(x+y)² é: ", r)
print("=================================")

