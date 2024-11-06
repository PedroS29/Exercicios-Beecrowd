def dicionario_para_lista_ordenada():
    dicionario = {}
    n = int(input("Quantos pares chave-valor você deseja inserir? "))
    for _ in range(n):
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        dicionario[chave] = valor
    lista_tuplas = list(dicionario.items())
    lista_tuplas.sort(key=lambda x: x[0])
    return lista_tuplas

# Exemplo de uso
lista_ordenada = dicionario_para_lista_ordenada()
print("Lista ordenada de tuplas:", lista_ordenada)
