#Condicional 
#Fazer um programa que leia a idade e informar se é maior ou menor de idade

idade = int(input("Informe sua idade: "))

if idade >17:
    print("Maior de idade")
else:
    print("Menor de idade")

#Criar um programa que leia a nota do aluno (float) 
#Dê a a mesagem "aprovado" se nota >=6 se não, de a mensagem "reprovado"

nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#Faça um programa que leia a senha do usuário

senha = input("Digite a senha: ")

if senha == "aluno123":
    print("Senha correta")
else:
    print("Senha Incorreta")