n = int(input())
vetor = [0]*n

alunos = input().split()
for i in range(n):
    vetor[i] = int(alunos[i])

vetor.sort()
mais_frequente = vetor.count(vetor[0])

for i in range(n):
    frequencia = vetor.count(vetor[i])
    if frequencia >= mais_frequente:
        mais_frequente = vetor.count(vetor[i])
        nummaisfrequente = vetor[i]

print(nummaisfrequente)