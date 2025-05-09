#Atividades relacionadas sobre Def

#Exercício 1


def mostrar_mensagem(mensagem, numero):
    print("Mensagem:", mensagem)
    print("Número:", numero)


if __name__ == '__main__':
    mensagem = input("Digite uma mensagem: ")
    numero = int(input("Digite um número: "))
    mostrar_mensagem(mensagem, numero)


#Exercício 2

def calcula_nascimento(p_valor):
    ano=2025 - p_valor
    return ano

if __name__=='__main__':
    valor=int(input('Qual é o seu ano de nascimento ?'))
    print("A sua idade é",calcula_nascimento(valor))




#Exercício 3

def numero(valor1,valor2,valor3):
    soma=valor1+valor2+valor3
    return soma

if __name__=='__main__':
    n1=int(input("Escreva um valor"))
    n2=int(input("Escreva outro valor"))
    n3=int(input("Escreva um outro valor"))
    print("A soma dos 3 valores é",numero(n1,n2,n3))



#Exercício 4

def calcula_media(valor1,valor2,valor3):
    media=(valor1+valor2+valor3)/3
    return media

if __name__=="__main__":
    nota1=int(input("Nota no 1º trimestre"))
    nota2=int(input("Nota no 2º trimestre"))
    nota3=int(input("Nota no 3º trimestre"))
    media_final = calcula_media(nota1, nota2, nota3)
    print(f"A media do ano do aluno é {media_final:.2f}")