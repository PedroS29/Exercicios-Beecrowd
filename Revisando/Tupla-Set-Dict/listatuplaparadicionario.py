# a)
def lista_para_dicionario():
    lista_de_tuplas = []
    n = int(input("Quantas tuplas você deseja inserir? "))
    for _ in range(n):
        chave = input("Digite o primeiro componente da tupla: ")
        valor = input("Digite o segundo componente da tupla: ")
        lista_de_tuplas.append((chave, valor))
    return {t[0]: t[1] for t in lista_de_tuplas}

# Exemplo de uso
dicionario = lista_para_dicionario()
print("Dicionário gerado:", dicionario)
