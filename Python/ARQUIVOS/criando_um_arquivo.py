arquivo = open("Casdastro_de_nome.txt","w")
arquivo.close()
arquivo = open('Casdastro_de_nome.txt','w')
nome_cliente = str(input("Digite o nome do cliente: "))
arquivo.write(nome_cliente)
arquivo.close()

arquivo = open("Casdastro_de_nome.txt","r")
print(arquivo.read())


