pessoas = int(input())
fila_inicial = []

x = input().split()
for i in range(pessoas):
    fila_inicial.append(int(x[i]))

desistentes = int(input())
fila_atual = []

y = input().split()
for i in range(desistentes):
    fila_atual.append(int(y[i]))

    if fila_atual[i] in fila_inicial:
        fila_inicial.remove(fila_atual[i])
        
for i in range(len(fila_inicial)):
    if i!=(len(fila_inicial)-1):
        print(fila_inicial[i], end=" ")
    else:
        print(fila_inicial[i])