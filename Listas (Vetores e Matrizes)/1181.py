l = int(input())
t = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)

soma = 0
media = 0
cont = 0

for j in matriz[l]:
    soma += j
    cont += 1

if t == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/cont:.1f}')