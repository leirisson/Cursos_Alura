def calcular_probabilidade_repeticao(lista, numero):
    total_elementos = len(lista)
    ocorrencias = lista.count(numero)
    probabilidade = ocorrencias / total_elementos
    return probabilidade

# Exemplo de uso
minha_lista = [1, 2, 3, 4, 5, 2, 3, 2, 4, 2]
meu_numero = 2

probabilidade_repeticao = calcular_probabilidade_repeticao(minha_lista, meu_numero)
print(f"A probabilidade de repetição do número {meu_numero} na lista é de {probabilidade_repeticao:.2f}")
