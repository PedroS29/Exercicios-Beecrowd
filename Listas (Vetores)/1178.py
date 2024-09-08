n = float(input())

vetor = []
vetor.append(n)

for i in range(1,100):
    vetor.append(n)
    vetor[i] = vetor[i-1]/2.0

for i in range(100):
    print(f'N[{i}] = {vetor[i]:.4f}')