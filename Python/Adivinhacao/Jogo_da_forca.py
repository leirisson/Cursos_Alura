import os

def joagar():
    print("*******************************")
    print("**Bem vindo ao Jogo da Forca***")
    print("*******************************")

    #------------------------------------------------
    #Adcionando interação com arquivo txt

    arquivo = open("palavras.txt","r")
    lista_de_palavras = []
    for para_cada_linha in arquivo:
        print(os.getcwd(arquivo))
        para_cada_linha = para_cada_linha.strip() # retirando a barra n e tambem rtirando os epassos
        lista_de_palavras.append(para_cada_linha)

    arquivo.close()
    #------------------------------------------------
    print(lista_de_palavras)
    palavra_secreta = 'tijolo'.upper()
    palavra_certa = ["_" for letra in palavra_secreta]


    erros = 0

    enforcou = False
    acertou = False

    letras_acertadas = ['_', '_', '_', '_', '_']

    while( not enforcou and not acertou):

        chute = str(input("Qual letra: ")).upper().strip()

    
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
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