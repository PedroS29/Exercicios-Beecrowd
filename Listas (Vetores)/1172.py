vetor = []

for i in range(10):
    x = int(input())
    vetor.append(x)

for i in range(10):
    if vetor[i] <= 0:
        vetor[i] = 1
    print(f'X[{i}] = {vetor[i]}')