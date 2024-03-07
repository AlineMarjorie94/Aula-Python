#Exercicios 29/02
print ("Eu sou d+!")

nome=input("Informe Seu Nome: ")
print("Seu nome " + nome +" é lindo")

#Questionario
print("Questionário")
N=input("Informe seu nome: ")
I=input("Informe sua idade: ")
C=input("Informe sua cidade: ")
print("Nome: " + N)
print("Idade: " + I)
print("Cidade: " + C)

#Exercicio Idade
I=int(input("Qual sua idade? "))
ano=2024-I
print("Ano aproximado de nascimento: "+str(ano))

#Criar um programa: - pergunte a idade - calcular dias = idade*365 - Dar mensagem apropiada
I=int(input("Qual é sua idade? "))
valor = I * 365
print ("Você viveu aproximadamente " +str(valor) +" dias")

# -Perguntar ao usuario a quantidade de horas -Calcular em minutos minutos=horas*60 -Dar mensagem apropriada
horas = int(input("Qauntidade de horas: "))
minutos = horas*60
print("O valor total em minutos é: " + str(minutos))

#Perguntar para o usuario o total de reais - Calcular quantos centavos são, centavos=reias*100 - Mostrar mensagem apropriada
reais = int(input("Valor total em reais: R$ ")) 
centavos = reais*100
print("O valor em centavos é: " + str(centavos))

# - Leia um numero inteiro do usuario na variavel N1 -Leia outro numero inteiro do usuario na variavel N2 -Calcule a soma da duas variaveis, soma=N1+N2 -Mostrar Resultados

N1 = int(input("Insira o valor 1: "))
N2 = int(input("Insira o valor 2: "))
soma = N1+N2
print("A soma dos dois valores é: " + str(soma))

#Leia do usuario um valor em dolares e converta para real
dolares = float(input("Insira o valor em dolares: US$"))
reais = dolares*4.97
print("O valor em reais é: R$ " + str(reais))

# -Leia do usuario o tamanho de um lado do quadrado e cacule a area
lado=float(input("Insira o tamanho do lado do quadrado: "))
area = lado*4
print("A area do quadrado é: " +str(area))

#multiplicação
N1 = float(input("Insira o valor 1: "))
N2 = float(input("Insira o valor 2: "))
multiplicacao = N1*N2
print("A Multiplicação dos dois valores é: " + str(multiplicacao))

#-Leia do usuario a sua idade e mostre quantas horas já viveu

idade = int(input("Insira sua idade: "))

ano = 24 * 365

horas = idade * ano

print("Você ja viveu " + str(horas) + " horas") 
