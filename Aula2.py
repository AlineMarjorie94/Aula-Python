#Exercicios 07/03/2024 

Leia do usuario o raio do círculo 
#Calcule área: area = 31415*raio*raio, mostre a area com mensagem apropriada
raio = float(input("Digite o raio do circulo: "))

area = 3.1415 * (raio*raio)

print("O valor da área do circulo é: " +str(area) +" cm²")

#Faça um programa que leia do usuario a temperatura em celcius e mostre em fahrenheit
celcius = float(input("Digite a temperatua em celcius: "))
fahrenheit = (celcius * 1.8)+32
print("A temperatura em fahrenheit é: " + str(fahrenheit) + "°F")

#Faça um programa que:
#Leia do usuario a nota 1
#Leia do usiario a nota 2
#Calcule a média como média = nota1 * 0.5 + nota2 * 0.5
#Mostre a mensagem apropriada

print("===================================")
nota1 = float (input("Digite a nota 1: "))
print("===================================")
nota2 = float (input("Digite a nota 2: "))

media = (nota1*0.5)+(nota2*0.5)
print("===================================")
print("O valor da media é: " +str(media))

#Faça programa que leia: -Nota TCC, -Nota prova, -Nota trabalho
#Calcule a média = TCC*0.3 + prova*0.5 + trabalho*0.2

tcc = float(input("Digite  a nota do TCC: "))
print("===================================")
prova = float(input("Digite a nota da prova: "))
print("===================================")
trabalho = float(input("Digite a nota do trabalho: "))
print("===================================")
 
média = (tcc*0.3) + (prova*0.5) + (trabalho*0.2) 

print ("O valor da média é: " +str(média))

#Faça um prograna que calcule Delta da formula de Bhaskara Δ = b²-4.a.c
print("===================================")
A = float(input("Digite o valor de A: "))
print("===================================")
B = float(input("Digite o valor de B: "))
print("===================================")
C = float(input("Digite o valor de C: "))
print("===================================")

delta = B*B-4*A*C


print("O valor de Δ é: " +str(delta))

#Faça um programa que leia o total da conta do restante 
#Calcule a gorjeta de de 10% gorjeta=total * 10/100
#Calcule a conta com a gorjeta  conta = total + gorjeta
#Mostre o resultado 

print("===================================")
total = float(input("Qual o valor da conta? "))
print("===================================")
gorjeta = total * (10/100)
conta = total + gorjeta

print("O valor total da conta é: R$ " + str(round(conta, 2)))

#Faça um programa que leia: peso e altura
#Calcule o imc = peso : altura²
#Mostre o IMC

print("===================================")
peso = float(input("Digite seu peso em kilos: "))
print("===================================")
altura = float(input("Digite sua altura em metros: "))
print("===================================")

imc = peso/(altura*altura)

print("Seu IMC é: "+ str(round(imc ,2)))

#Faça um programa que leia: O total da compra, o valor do desconto, o valor dos juros 
#Calcule a conta total total = total-desconto+juros
print("===================================")
total = float(input("Digite o valor da compra: R$ "))
print("===================================")
desconto = float(input("Digite o valor do desconto: R$ "))
print("===================================")
juros = float(input("Digite o valor dos juros: R$ "))
print("===================================")

total = total - desconto + juros

print("O valor total da compra é: R$ "+str(round(total ,2)))

#Faça um programa que leia uma distancia em metros e mostre: Em centimetros e em milimetros

print("===================================")
metro = float(input("Digite a distancia: "))

centimetro = metro * 100
print("===================================")
milimetro = metro * 1000

print ("A distancia percorrida é de: " + str(centimetro)+ " centimentros")
print("===================================")
print ("A distancia percorrida é de: " + str(milimetro)+ " milimentros")

#Faça um programa que leia: nome, nome do meio e sobrenome 
#Mostre o nome completo com as palavras separadas por um espaço em branco
print("===================================")
N = (input("Digite o nome: "))
print("===================================")
NM = (input("Digite o nome do meio: "))
print("===================================")
S = input("Digite o sobrenome: ")

NC = N+" "+NM+" "+S
print("Seu nome completo é: " +NC)

#Faça um programa que leia um valor em reias e mostre em: Dolares, euros, pesos e ienes
print("===================================")
real = float(input("Insira o valor em reais: R$ " ))
print("===================================")
dolares = real / 4.94
euros = real / 5.40
pesos = real / 0.29
ienes = real / 0.03

print ("O valor em dolares é: US$ "+str(round(dolares ,2)))
print("===================================")
print ("O valor em euros é: € "+str(round(euros ,2)))
print("===================================")
print ("O valor em pesos é: MX$ "+str(round(pesos ,2)))
print("===================================")
print ("O valor em ienes é: ¥ "+str(round(ienes ,2)))



