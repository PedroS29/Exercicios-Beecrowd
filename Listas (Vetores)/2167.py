n = int(input())
vetor = [0]*n

r = input().split()

for i in range(n):
    vetor[i] = int(r[i])

queda = 0

for i in range(1,n):
    if vetor[i] < vetor[i-1]:
        queda = i+1
        break
print(queda)