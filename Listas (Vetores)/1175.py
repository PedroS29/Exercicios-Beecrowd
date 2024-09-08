vetor = []

for i in range(20):
    x = int(input())
    vetor.append(x)

for i in range(10):
    j = 19-i
    vetor[i], vetor[j] = vetor[j], vetor[i]

for i in range(20):
    print(f'N[{i}] = {vetor[i]}')