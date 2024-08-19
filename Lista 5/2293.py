entrada = input().split()
n = int(entrada[0])
m = int(entrada[1])

matriz = []

for i in range(n):
    linha = []
    x = input().split()
    for j in range(m):
        linha.append(int(x[j]))
    matriz.append(linha)

maior_linha = 0
maior_coluna = 0

for i in range(n):
    soma_linha = sum(matriz[i])
    if soma_linha > maior_linha:
        maior_linha = soma_linha

for j in range(m):
    soma_coluna = 0
    for i in range(n):
        soma_coluna += matriz[i][j]
    if soma_coluna > maior_coluna:
        maior_coluna = soma_coluna

resultado = max(maior_linha, maior_coluna)
print(resultado)