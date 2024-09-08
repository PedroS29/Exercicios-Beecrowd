while True:
    n = int(input())
    if n == 0:
        break

    matriz = []

    for i in range(n):
        linha = []
        for j in range(n):
            valor = min(i, j, n - 1 - i, n - 1 - j) + 1
            linha.append(valor)
        matriz.append(linha)

    for linha in matriz:
        for i in range(len(linha)):
            if i != len(linha) - 1:
                print(f"{linha[i]:3}", end=" ")
            else:
                print(f"{linha[i]:3}")
    print() 