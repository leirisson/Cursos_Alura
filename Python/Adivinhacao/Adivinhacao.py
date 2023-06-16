import random


def jogar():
    print("*******************************")
    print("Bem vindo ao Jogo de Advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1

    print("Qual o nivel de dificuldade ?")
    print("(1) Facil (2) Medio (3)Dificil")

    nivel = int(input("Escolha o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range( 1, total_de_tentativas +1):
        print(f"Tentaiva {rodada} de {total_de_tentativas}")

        chute = int(input("Chue um valor de 0 a 10: "))

        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto
        chute_certo  = numero_secreto == chute

        if(chute < 1 or chute > 100):
            print("Valor invalido informe um valor entre 1 e 100")
            continue

        if(chute_certo):
            print("Você ACERTOU !!!")
            print(f"o numero secreto é: {numero_secreto} e voce informou {chute}")
            break
        else:
            if(chute_maior):
                print(f"Voce Errou o seu chute foi maior que o numero secreto")
            elif(chute_menor):
                print("Você Errou !!!")
                print(f"o seu chute foi menor que o numero secreto !")


if(__name__ == "__name__"):
    jogar()