n = int(input())

palavras = input().split()

for i in range(n):
    if (palavras[i][:2] == 'OB' or palavras[i][:2] == 'UR') and len(palavras[i]) == 3:
        palavras[i] = palavras[i][:2] + 'I'

print(' '.join(palavras))