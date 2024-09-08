while True:
    n = int(input())

    if n == 0:
        break

    resultado =  []

    for i in range(1,(n+1)):
        linha = []
        count = i
        for j in range(n):
            linha.append(abs(count))
            if(count == 1):
                count -= 3
            else:
                count -= 1
        resultado.append(linha)

    for i in range(n):
        resposta = ''
        for j in range(n):
            resposta += " %3d" %resultado[i][j]
        print(resposta[1:])
    print("")