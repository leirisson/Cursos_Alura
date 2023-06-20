def joagar():
    print("*******************************")
    print("**Bem vindo ao Jogo da Forca***")
    print("*******************************")

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    letras_acertadas = ['_', '_', '_', '_', '_']

    while( not enforcou and not acertou):
        chute = input("Qual letra: ")
        chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() in letra.upper()):
                letras_acertadas[index] = letra
            index += 1
        print(f"{letras_acertadas}")


if(__name__ == "__main__"):
    joagar()