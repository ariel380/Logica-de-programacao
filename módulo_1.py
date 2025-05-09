
raio=float(input('Qual é o volume ?'))
pi=3.14159
volume=(4/3)*pi*raio**3
print(f'O volume de uma esfera de raio R é {volume:.2f}')


#Exercício 2 

massa=float(input("Qual é o seu KG ?"))
calculo=massa*0.03
print("A quantidade ideal de água necessária para sua sobrevivência é",calculo, "litros")


#Exercício 3

x1=float(input("Insira o valor do x ponto 1 "))
y1=float(input("Insira o valor do y do ponto 1 "))
x2=float(input("Insira o valor do x do ponto 2 "))
y2=float(input("Insira o valor do y do ponto 2 "))

distancia=((x2-x1)**2+(y2-y1)**2)**0.5
print("A distãncia entre eles é",distancia)



#Exercício 4

valor1=int(input("Descreva um valor"))
valor2=int(input("Descreva segundo valor"))

if valor1>valor2:
	print("a ordem crescente dos valores fornecidos é",valor2,valor1)
else:
	print("a ordem crescente dos valores fornecidos é",valor1,valor2)


#Exercício 5

altura= float(input("Qual é sua altura ?"))
Genero= input("Escreva M para genêro masculino e F para gênero feminino ")
if Genero=='M':
	print(f"O seu peso ideial é ", (72.7 * altura) - 58)
else:
	print(f"O seu peso ideial é", (62.1 * altura) - 44.7)


