while True:
    assassinos = []
    n = int(input())
    if n == 0:
        break

    x = input().split()
    for i in range(n):
        assassinos.append(int(x[i]))

    mais_suspeito = max(assassinos)
    segundo_maior = -float('inf')
    indice = -1

    for i in range(n):
        if segundo_maior < assassinos[i] and assassinos[i] != mais_suspeito:
            segundo_maior = assassinos[i]
            indice = i

    print(indice + 1)