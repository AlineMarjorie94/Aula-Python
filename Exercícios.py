#Construa um algoritmo que, tendo como dados de entrada dois pontos 
#quaisquer no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles. 
#A fórmula que efetua tal cálculo é:

import math
print("==================")

x1 = float(input("Digite o valor de x1: "))
x2 = float(input("Digite o valor de x2: "))
y1 = float(input("Digite o valor de y1: "))
y2 = float(input("Digite o valor de y2: "))

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("==================")
print("A distancia é:", str(round(distancia, 2)))

#2.	Escreva um algoritmo que leia três números inteiros e positivos 
#(A, B, C) e calcule a seguinte expressão:

print("==================")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

R = (A+B)**2
S = (B+C)**2

D = (R+S)/2

print("==================")

print("O Valor da expressão é:",D)

#Faça um algoritmo que leia a idade de uma pessoa 
#expressa em anos, meses e dias e mostre-a  expressa 
#apenas em dias.

print("==================")
anos = int(input("Informe sua idade em anos: "))
meses = int(input("Informe o restante da idade em meses: "))
dias = int(input("Informe o restante da idade em dias: "))

idade_em_dias = anos * 365 + meses * 30 + dias

print("==================")
print("Sua idade em dias é aproximadamente: " + str(idade_em_dias))

#Faça um algoritmo que leia a idade de uma pessoa expressa 
#em dias e mostre-a expressa em anos, meses e dias

print("==================")
idadeemdias = int(input("Informe sua idade em dias: "))

anos = idadeemdias // 365
meses = (idadeemdias % 365) // 30
dias = (idadeemdias % 365) % 30
print("==================")
print("Sua idade é aproximadamente:", anos,"anos", meses, "meses e ", dias, "dias")

#Faça um algoritmo que leia as 3 notas de um aluno e calcule a média 
#final deste aluno. Considerar que a média é ponderada e que o peso 
#das notas é: 2,3 e 5, respectivamente.

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))

peso1 = 2
peso2 = 3
peso3 = 5

médiafinal = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3)/10

print("A nota final é:", médiafinal)

#Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica 
#expressa em segundos e mostre-o expresso em horas, minutos e segundos.

duracaoemsegundos = int(input("Digite o tempo de duração do evento em segundos: "))

horas = duracaoemsegundos // 3600
resto_segundos = duracaoemsegundos % 3600
minutos = resto_segundos // 60
segundos = resto_segundos % 60

print("O evento durou: ", horas, "horas", minutos, "minutos e", segundos, "segundos")

#O custo ao consumidor de um carro novo é a soma do custo de fábrica 
#com a percentagem do distribuidor e dos impostos (aplicados ao custo 
#de fábrica). Supondo que a percentagem do distribuidor seja de 28% e 
#os impostos de 45%, escrever um algoritmo que leia o custo de fábrica 
#de um carro e escreva o custo ao consumidor.

custodefabrica = float(input("Digite o custo de fábrica do carro: "))

distribuidor = 0.28
imposto = 0.45

custoconsumidor = custodefabrica + (distribuidor * custodefabrica) + (imposto * custodefabrica)

print("O custo ao consumidor do carro é:", custoconsumidor)

#8.	Um sistema de equações lineares do tipo:ax+b = c dx+ey = f, 
#pode ser resolvido segundo mostrado abaixo: x = ce-bf/ae-bd y= af-cd/ae-bd

print("==================")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))
f = float(input("Digite o valor de f: "))

x = ((c*e)-(b*f)/(a*e)-(b*d))
y= ((a*f)-(c*d)/(a*e)-(b*d))

print("==================")
print ("O resultado de x é:", x, " e resultado y é:", y)

#Calcule a média aritmética das 3 notas de um aluno e mostre, 
#além do valor da média, uma mensagem de "Aprovado", caso a média 
#seja igual ou superior a 6, ou a mensagem "reprovado", caso contrário.

print("==================")
nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))

médiafinal = (nota1 + nota2 + nota3)/3

if médiafinal >=6:
    print("A média final é: ",médiafinal, "o aluno está aprovado!")
else:
    print("A média final é: ",médiafinal, "o aluno está reprovado!")

#Elaborar um algoritmo que lê 3 valores a,b,c e os escreve. A seguir,
#encontre o maior dos 3 valores e o escreva com a mensagem : "É o maior".
#a + b + | a - b |
#Maior de a e b = ------------------

print("==================")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print("==================")
if a > b and a > c:
    print("O Maior valor é A")
elif b > a and b > c:
    print("O Maior valor é B")
elif c > a and c > b:
    print("O Maior valor é C") 
else:
    print("Não há valor maior") 

#Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".

print("==================")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

if  a % b == 0 or b % a == 0:
    print("São múltiplos")
else: 
    print("Não são múltiplos")

#Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:
#infantil A = 5 - 7 anos
#infantil B = 8-10 anos
#juvenil A = 11-13 anos
#juvenil B = 14-17 anos
#adulto = maiores de 18 anos  

print("==================")

idade = int(input("Insira a idade do nadador: "))

print("==================")
if idade >= 5 and idade <= 7:
    print("Categoria: infantil A")
elif idade >= 8 and idade <= 10:    
    print("Categoria: infantil B")
elif idade >= 11 and idade <= 13:       
    print("Categoria: juvenil A")
elif idade >= 14 and idade <= 17:  
    print("Categoria: juvenil B")
elif idade >= 18:
    print("Categoria: adulto")
else: 
    print("Idade fora das categorias válidas.")

#Escreva um algoritmo que leia 3 números inteiros e mostre o maior deles.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))    

if num1 > num2 and num1 > num3:
    print("O valor maior é: ",num1)
elif num2 > num1 and num2 > num3:
    print("O valor maior é: ",num2)
elif num3 > num1 and num3 > num2:
    print("O valor maior é: ",num3)
else: 
    print("Os valores são iguais")        

#Escreva um algoritmo que leia o código de um aluno e suas três notas.
#Calcule a média ponderada do aluno, considerando que o peso para a maior
#nota seja 4 e para as duas restantes, 3. Mostre o código do aluno, suas 
#três notas, a média calculada e uma mensagem "APROVADO" se a média for maior 
#ou igual a 5 e "REPROVADO" se a média for menor que 5.

codigo_aluno = input("Digite o código do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = nota1 * 0.3 + nota2 * 0.3 + nota3 * 0.4

if media >=5:
    print ("A média do aluno", codigo_aluno, "será de:", round(media, 2), ". Aluno aprovado!")
else:
    print ("A média do aluno", codigo_aluno, "será de:", round(media, 2), ". Aluno Reprovado!")

 #Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando 
#se este número é  par ou ímpar, e se é positivo ou negativo.,

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#O cardápio de uma lancheria é o seguinte:
#Especificação	 Código Preço
#Cachorro quente	100	1,20
#Bauru simples	    101	1,30
#Bauru com ovo	    102	1,50
#Hambúrger	        103	1,20
#Cheeseburguer	    104	1,30
#Refrigerante	    105	1,00
#Escrever um algoritmo que leia o código do item pedido, 
#a quantidade e calcule o valor a ser pago por aquele lanche. 
#Considere que a cada execução somente será calculado um item.

print("==================")
codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

if codigo == 100:
    valor = 1.20
elif codigo == 101:
    valor = 1.30
elif codigo == 102:
    valor = 1.50
elif codigo == 103:
    valor = 1.20
elif codigo == 104:
    valor = 1.30
elif codigo == 105:
    valor = 1.00
else:
    print("Código do item inválido.")

total = valor * quantidade

print ("O valor total é:", round(total, 2))

#Tendo como dados de entrada a altura e o sexo de uma pessoa 
#(?M? masculino e ?F? feminino), construa um algoritmo que calcule 
#seu peso ideal, utilizando as seguintes fórmulas:
#-	para homens: (72.7*h)-58
#-	para mulheres: (62.1*h)-44.7

print("==================")

altura = float(input("Digite sua a altura: "))
sexo = input("Digite o seu sexo(M masculino e F feminino): ")

if sexo == 'M':
     pesoideal = (72.7 * altura)-58
     print("Seu peso ideal é:", round(pesoideal, 2), "kg")
elif sexo == 'F':
     pesoideal =(62.1 * altura)-44.7
     print("Seu peso ideal é:", round(pesoideal, 2), "kg")
else:
     print("Sexo inválido. Por favor, insira M para masculino ou F para feminino.")

#Um banco concederá um crédito especial aos seus clientes, 
#variável com o saldo médio no último ano. Faça um algoritmo 
#que leia o saldo médio de um cliente e calcule o valor do crédito 
#de acordo com a tabela abaixo. Mostre uma mensagem informando o saldo 
#médio e o valor do crédito. (use o comando caso-de e não faça repetições)

#Saldo médio	Percentual
#de 0 a 200	    nenhum crédito
#de 201 a 400	20% do valor do saldo médio
#de 401 a 600	30% do valor do saldo médio
#acima de 601	40% do valor do saldo médio

saldomedio = float(input("Digite o saldo médio do cliente: "))

if saldomedio >= 0 and saldomedio <= 200:
    percentual = 0
elif saldomedio <= 400:
    percentual = 0.20
elif saldomedio <= 600:
    percentual = 0.30
else:
    percentual = 0.40

credito = percentual * saldomedio

print("Saldo médio:", round(saldomedio,2))
print("Valor do crédito:", round(credito,2))

#Um usuário deseja um algoritmo onde possa escolher que 
#tipo de média deseja calcular a partir de 3 notas. Faça um algoritmo 
#que leia as notas, a opção escolhida pelo usuário e calcule a média.
#1	-aritmética
#2	-ponderada (3,3,4)
#3	-harmônica

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
opcao = int(input("Escolha o tipo de média a ser calculada:\n1 - Aritmética\n2 - Ponderada (3, 3, 4)\n3 - Harmônica\n"))

if opcao == 1:
    media = (nota1 + nota2 + nota3) / 3
    tipo_media = "aritmética"
elif opcao == 2:
    media = (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10
    tipo_media = "ponderada"
elif opcao == 3:
    media = 3 / (1/nota1 + 1/nota2 + 1/nota3)
    tipo_media = "harmônica"
else:
    print("Opção inválida.")

print("A média", tipo_media, "das notas é:", round(media,2))

#Um vendedor necessita de um algoritmo que calcule o preço total 
#devido por um cliente. O algoritmo deve receber o código de um produto 
#e a quantidade comprada e calcular o preço total, usando a tabela abaixo:
#Código do Produto	Preço unitário
#1001	            5,32
#1324	            6,45
#6548	            2,37
#0987	            5,32
#7623	            6,45

codigoproduto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

if codigoproduto == 1001:
    precounitario = 5.32
elif codigoproduto == 1324:
    precounitario = 6.45
elif codigoproduto == 6548:
    precounitario = 2.37
elif codigoproduto == 987:
    precounitario = 5.32
elif codigoproduto == 7623:
    preco_unitario = 6.45
else:
    print("Código do produto inválido.")

precototal = precounitario * quantidade
print("Preço total:", round(precototal,2))

#Um vendedor precisa de um algoritmo que calcule o preço total devido por um cliente. 
#O algoritmo deve receber o código de um produto e a quantidade comprada e calcular o
# preço total, usando a tabela abaixo. Mostre uma mensagem no caso de código inválido.
#Código	      Preço unitário
#'ABCD'	      R$ 5,30
#'XYPK'	      R$ 6,00
#'KLMP'	      R$ 3,20
#'QRST'	      R$ 2,50
codigo = input("Digite o código do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))

if codigo == "ABCD":
    preco = 5.30
elif codigo == "XYPK":
    precounitario = 6.00
elif codigo == "KLMP":
    precounitario = 3.20
elif codigo == "QRST":
    precounitario = 2.50
else:
    print("Código do produto inválido.")

precototal = precounitario * quantidade
print("Preço total:",round(precototal,2))


#Uma empresa concederá um aumento de salário aos seus funcionários, 
#variável de acordo com o cargo, conforme a tabela abaixo. Faça um algoritmo 
#que leia o salário e o cargo de um funcionário e calcule o novo salário. 
#Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 
#40% de aumento. Mostre o salário antigo, o novo salário e a diferença.
#Código	Cargo	  Percentual
#101	Gerente	    10%
#102	Engenheiro	20%
#103	Técnico	    30%

salario = float(input("Digite o salário do funcionário: "))
cargo = int(input("Digite o código do cargo do funcionário: "))

if cargo == 101:
    aumento_percentual = 0.10
elif cargo == 102:
    aumento_percentual = 0.20
elif cargo == 103:
    aumento_percentual = 0.30
else:
    aumento_percentual = 0.40
    print("Cargo não encontrado na tabela. Recebendo 40% de aumento.")

novosalario = salario * (1 + aumento_percentual)
diferencasalario = novosalario - salario
print("Salário antigo:", salario)
print("Novo salário:", round(novosalario,2))
print("Diferença:", round(diferencasalario,2))

#Elaborar um algoritmo que lê 3 valores a,b,c e verifica se eles 
#formam ou não um triângulo. Supor que os valores lidos são inteiros 
#e positivos. Caso os valores formem um triângulo, calcular e escrever 
#a área deste triângulo. Se não formam triângulo escrever os valores lidos. 
#( se a > b + c não formam triângulo algum, se a é o maior).

a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

if a < b + c and b < a + c and c < a + b:
    # Calcular o semiperímetro
    s = (a + b + c) / 2
    # Calcular a área usando a fórmula de Heron
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Os valores formam um triângulo.")
    print("Área do triângulo:", round(area,2))
else:
    print("Os valores fornecidos não formam um triângulo.")

#Escrever um algoritmo que lê a hora de início de um jogo 
#e a hora do final do jogo (considerando apenas horas inteiras) 
#e calcula a duração do jogo em horas, sabendo-se que o tempo 
#máximo de duração do jogo é de 24 horas e que o jogo pode 
#iniciar em um dia e terminar no dia seguinte.

inicio = int(input("Digite a hora de início do jogo: "))
final = int(input("Digite a hora do final do jogo: "))

if final >= inicio:
    duracao = final - inicio
else:
    duracao = 24 - inicio + final

print("A duração do jogo foi de", duracao, "horas.")
#Escrever um algoritmo que lê um conjunto de 4 valores i, a, b, c,
#onde i é um valor inteiro e positivo e a, b, c, são quaisquer valores 
#reais e os escreva. A seguir:

#a)	Se i=1 escrever os três valores a, b, c em ordem crescente.
#b)	Se i=2 escrever os três valores a, b, c em ordem decrescente.
#c)	Se i=3 escrever os três valores a, b, c de forma que o maior entre a, b, c fique dentre os dois.

i = int(input("Digite o valor de i: "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if i == 1:
    lista_valores = [a, b, c]
    lista_valores.sort()
    print("Valores em ordem crescente:", lista_valores)
elif i == 2:
    lista_valores = [a, b, c]
    lista_valores.sort(reverse=True)
    print("Valores em ordem decrescente:", lista_valores)
elif i == 3:
    maior = max(a, b, c)
    menor = min(a, b, c)
    meio = (a + b + c) - maior - menor
    print("Valores com o maior entre a, b, c no meio:", menor, meio, maior)
else:
    print("Valor de i inválido.")


#Escrever um algoritmo que lê um valor em reais e calcula qual o menor 
#número possível de notas de 100, 50, 10, 5 e 1 em que o valor lido 
#pode ser decomposto. Escrever o valor lido e a relação de notas necessárias

valor = int(input("Digite o valor em reais: "))

notas100 = valor // 100
resto = valor % 100
notas50 = resto // 50
resto %= 50
notas10 = resto // 10
resto %= 10
notas5 = resto // 5
resto %= 5
notas1 = resto

print("Valor lido:", valor, "reais")
print("Notas necessárias:")
print("Notas de 100:", notas100)
print("Notas de 50:", notas50)
print("Notas de 10:", notas10)
print("Notas de 5:", notas5)
print("Notas de 1:", notas1)

#Escrever um algoritmo que lê:
#-	a percentagem do IPI a ser acrescido no valor das peças
#-	o código da peça 1, valor unitário da peça 1, quantidade de peças 1
#-	o código da peça 2, valor unitário da peça 2, quantidade de peças 2
#O algoritmo deve calcular o valor total a ser pago e apresentar o resultado.
#Fórmula : (valor1*quant1 + valor2*quant2)*(IPI/100 + 1)


ipipercentagem = float(input("Digite a percentagem do IPI a ser acrescido (%): "))

codigopeca1 = input("Digite o código da peça 1: ")
valorunitariopeca1 = float(input("Digite o valor unitário da peça 1: "))
quantidadepeca1 = int(input("Digite a quantidade de peças 1: "))

codigopeca2 = input("Digite o código da peça 2: ")
valorunitariopeca2 = float(input("Digite o valor unitário da peça 2: "))
quantidadepeca2 = int(input("Digite a quantidade de peças 2: "))

valortotal = (valorunitariopeca1 * quantidadepeca1 + valorunitariopeca2 * quantidadepeca2) * (ipipercentagem / 100 + 1)

print("Valor total a ser pago:", round(valortotal,2))

#Escrever um algoritmo que lê a hora de início e hora de término de um jogo, 
#ambas subdivididas em dois valores distintos: horas e minutos. Calcular e 
#escrever a duração do jogo, também em horas e minutos, considerando que o 
#tempo máximo de duração de um jogo é de 24 horas e que o jogo pode iniciar 
#em um dia e terminar no dia seguinte.

iniciohoras = int(input("Digite a hora de início (horas): "))
iniciominutos = int(input("Digite a hora de início (minutos): "))

terminohoras = int(input("Digite a hora de término (horas): "))
terminominutos = int(input("Digite a hora de término (minutos): "))

diferencaminutos = ((terminohoras * 60) + terminominutos) - ((iniciohoras * 60) + iniciominutos)

duracaohoras = diferencaminutos // 60
duracaominutos = diferencaminutos % 60

print("A duração do jogo foi de", duracaohoras, "horas e", duracaominutos, "minutos.")

#29.	Escrever um algoritmo que lê o número de identificação, 
#as 3 notas obtidas por um aluno nas 3 verificações e a média 
#dos exercícios que fazem parte da avaliação. Calcular a média 
#de aproveitamento, usando a fórmula:
#MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
#A atribuição de conceitos obedece a tabela abaixo:
#Média de
#Aproveitamento	Conceito
#9,0            	A
#7,5 e < 9,0    	B
#6,0 e < 7,5    	C
#4,0 e < 6,0	    D
#< 4,0          	E
#O algoritmo deve escrever o número do aluno, suas notas, a média dos 
#exercícios, a média de aproveitamento, o conceito correspondente e a mensagem:
# APROVADO se o conceito for A,B ou C e REPROVADO se o conceito for D ou E.


identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
exercicios = float(input("Digite a média dos exercícios: "))

aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + exercicios) / 7

if aproveitamento >= 9.0:
    conceito = "A"
elif 7.5 <= aproveitamento < 9.0:
    conceito = "B"
elif 6.0 <= aproveitamento < 7.5:
    conceito = "C"
elif 4.0 <= aproveitamento < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in ['A', 'B', 'C']:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print("Número de identificação:", identificacao)
print("Notas:", nota1, nota2, nota3)
print("Média dos exercícios:", round(exercicios,2))
print("Média de aproveitamento:", round(aproveitamento,2))
print("Conceito:", conceito)
print("Situação:", situacao)

#O departamento que controla o índice de poluição do meio ambiente 
#mantém 3 grupos de indústrias que são altamente poluentes do meio 
#ambiente. O índice de poluição aceitável varia de 0,05 até 0,25. 
#Se o índice sobe para 0,3 as indústrias do 1o grupo são intimadas 
#a suspenderem suas atividades, se o índice cresce para 0,4 as do 
#1o e 2o grupo são intimadas a suspenderem suas atividades e se o 
#índice atingir 0,5 todos os 3 grupos devem ser notificados a paralisarem 
#suas atividades. Escrever um algoritmo que lê o índice de poluição medido 
#e emite a notificação adequada aos diferentes grupos de empresas.

indicepoluicao = float(input("Digite o índice de poluição medido: "))

if indicepoluicao >= 0.5:
    print("Todos os 3 grupos devem ser notificados a paralisarem suas atividades.")
elif indicepoluicao >= 0.4:
    print("As indústrias do 1º e 2º grupo devem ser intimadas a suspenderem suas atividades.")
elif indicepoluicao >= 0.3:
    print("As indústrias do 1º grupo devem ser intimadas a suspenderem suas atividades.")
elif 0.25 >= indicepoluicao >= 0.05:
    print("O índice de poluição está dentro dos limites aceitáveis.")
else:
    print("O índice de poluição está abaixo do mínimo aceitável.")

#Escrever um algoritmo que calcule os sucessivos valores de E 
#usando a série abaixo e considerando primeiro 3 termos, 
#depois 4 termos e, por fim, 5 termos:
#E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / 4!

def fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def calcular_E(n):
    E = 1.0  
    if n >= 2:
        E += 1 / fatorial(1)
    if n >= 3:
        E += 1 / fatorial(2)
    if n >= 4:
        E += 1 / fatorial(3)
    if n >= 5:
        E += 1 / fatorial(4)
    if n >= 6:
        E += 1 / fatorial(5)
    return E

E_3 = calcular_E(3)
print("E com 3 termos:", E_3)

E_4 = calcular_E(4)
print("E com 4 termos:", E_4)

E_5 = calcular_E(5)
print("E com 5 termos:", E_5)
