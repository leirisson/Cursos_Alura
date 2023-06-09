print("*******************************")
print("Bem vindo ao Jogo de Advinhação")
print("*******************************")

numero_secreto = 5

chute = int(input("Chue um valor de 0 a 10: "))

if numero_secreto == chute:
    print("Você ACERTOU !!!")
    print(f"o numero secreto é: {numero_secreto} e voce informou {chute}")
else:
    print("Você Errou !!!")
    print(f"o numero secreto é: {numero_secreto} e voce informou {chute}")