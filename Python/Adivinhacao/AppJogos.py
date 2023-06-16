import Adivinhacao
import Jogo_da_forca

def escolhaJogo():
    print("*******************************")
    print("******* Escolha um jogo *******")
    print("*******************************")

    jogo = int(input("(1) Adivinhação  (2) Forca, Qual é a sua escolha:  "))

    if(jogo == 1):
        print("Jogo da forca")
        Adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogo da Forca")
        Jogo_da_forca.joagar()

if(__name__ == "__main__"): # função principal do programa
    escolhaJogo()