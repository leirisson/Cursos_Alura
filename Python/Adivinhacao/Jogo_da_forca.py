def joagar():
    print("*******************************")
    print("**Bem vindo ao Jogo da Forca***")
    print("*******************************")

    palavra_secreta = 'tijolo'.upper()
    palavra_certa = ["_" for letra in palavra_secreta]


    erros = 0

    enforcou = False
    acertou = False
    while( not enforcou and not acertou):

        chute = input("Qual letra: ")
        chute.upper().strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    palavra_certa[index] = letra
                index += 1
        else:
            erros +=1

        enforcou = erros == 6
        acertou = "_" not in palavra_certa

        print(palavra_certa)

    if(acertou):
        print('Voce ganhou')
    else:
        print("Voce perdeu")
if(__name__ == "__main__"):
    joagar()