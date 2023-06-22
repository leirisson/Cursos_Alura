gravar_nome = open("gravar_nome.txt","a")
nome = str(input("Qual seu nome: "))
gravar_nome.write(f"\n{nome}")
gravar_nome.close()


with open("gravar_nome.txt","r") as arquivo:
    conteu = arquivo.read()
    print(conteu)