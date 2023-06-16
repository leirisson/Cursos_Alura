def joagar():
    print("*******************************")
    print("**Bem vindo ao Jogo da Forca***")
    print("*******************************")

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False
    while( not enforcou and not acertou):
        chute = input("Qual letra: ")
        chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f"encontrei a letra {chute.upper()} na posição {index}")
            index += 1
        print("em loop")


if(__name__ == "__main__"):
    joagar()