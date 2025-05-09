#While

#Exercício 

print("A seguir irei mostrar uma quantidade de valores reais")

ct=0
ct2=1
soma=0
soma1=0
while ct<25:
    ct+=1
    soma=ct+soma
    print(ct)
    if ct>20:
        ct2 += 1
        soma1 += ct

méd=soma/ct


print("quantidade",ct,"soma",soma, "Quantidade de valores >20",ct2,"média aritmética",méd)

#Exercício 2

ct = 0
apr = 0
rep = 0

print("Insira o valor 11 para sair do programa ")
while True:
    nota = int(input("Qual a nota do aluno ? Digite 11 para sair do programa"))

    if nota==11:
        break

    nome = str(input("Qual o nome do(a) aluno(a)"))

    ct+=1

    if 0 <= nota <= 10:

        if nota>=5:
            apr+=1
            print("Aluno(a) aprovado ")

        elif 0 <= nota > 5:
            rep += 1
            print("Aluno(a) reprovado(a)")

    else:
        print("valor errado. Favor digitar novamente")


print(f"Quantidade total de alunos que fizeram a prova: {ct}")
print(f"Quantidade de alunos aprovados: {apr}")
print(f"Quantidade de alunos reprovados: {rep}")

#Exercício 3

print("Insira o número 0 para encerrar o programa")

soma_par = 0
soma_impar = 0
cont_par = 0
cont_impar = 0

while True:

    num=int(input("Insira valor e descobriremos para você se ele é ímpar ou par "))

    if num==0:
        print("Programa encerrado")
        break

    elif num%2==0:
        soma_par += num
        cont_par += 1
        print("Ele é um número par")


    else:
        soma_impar += num
        cont_impar += 1
        print("ele é um número ímpar")

media_par = soma_par / cont_par if cont_par > 0 else 0
media_impar = soma_impar / cont_impar if cont_impar > 0 else 0

print(f"A média aritmética do número par é {media_par}")
print(f"A média aritmética do número ímpar é {media_impar}")
