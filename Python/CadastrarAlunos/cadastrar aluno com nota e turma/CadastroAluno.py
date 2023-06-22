import os
def ExibirMenu():
    Titulo = "Sistema de cadastro de aluno"
    print("#"*len(Titulo))
    print(f"{Titulo}")
    print("1 - Cadastrar")
    print("2 - Listar Cadastro")
    print("0 - Para sair")
    print("#"*len(Titulo))

while True:
    ExibirMenu()
    op = int(input("Qual dua opção: "))
    if (op == 0):
        break
    elif(op == 1):
        Cadastro_Aluno = 0
        while True:
            Cadasdro_aluno = {"nome":"", "idade":"", "curso":""}
            datanascimento = str(input("Qual a data de nascimendo do aluno ex Dia-Mes-Ano: "))

            nome = str(input("Digite seu nome Completo: ")).strip().lower()
            caminho = f"Cadastros/{datanascimento}-{nome}.txt"

            with open(f'{caminho}', "w") as arquivo:
                Cadasdro_aluno['nome'] = nome
                Cadasdro_aluno['idade'] = int(input("Qual a idade do aluno: "))
                Cadasdro_aluno['curso'] = str(input("Qual o curso do aluno: "))
                arquivo.write(f"Nome: {Cadasdro_aluno['nome']}\nIdade: {Cadasdro_aluno['idade']}\nCurso: {Cadasdro_aluno['curso']}")
                op = str(input("Deseja continuar: [S/N]"))
                Cadasdro_aluno +=1
                if(op in 'Ss'):
                    continue
                else:
                    break

    elif op == 2:
        caminho = "Cadastros/"
        pasta_arquivos = os.listdir(caminho)

        for cadastros in pasta_arquivos:
            print(cadastros)




