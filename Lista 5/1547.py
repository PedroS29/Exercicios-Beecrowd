n = int(input())

for i in range(n):
    qt = 0
    s = 0
    alunos = []

    x = input().split()
    qt = int(x[0])
    s = int(x[1])

    y = input().split()
    for i in range(qt):
        alunos.append(int(y[i]))

    vencedor = 0
    menor_dif = float('inf')
    
    for i in range(qt):
        if alunos[i] == s:
            vencedor = i + 1
            break
        else:
            diferenca = abs(alunos[i] - s)
            if diferenca < menor_dif:
                menor_dif = diferenca
                vencedor = i + 1
    print(vencedor)