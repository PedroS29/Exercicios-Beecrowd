n = int(input())
vetor = [0]*n

x = input().split()

for i in range(n):
    vetor[i] = int(x[i])

menor = vetor[0]
posicao = 0

for i in range(n):
    if vetor[i] < menor:
        menor = vetor[i]
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')