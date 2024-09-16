n = int(input())

for i in range(n):
    palavras = input().split()

    for i in range(len(palavras)):
        if (palavras[i][1:9] == 'oulupukk') and len(palavras[i]) == 10:
            palavras[i] = 'J' + palavras[i][1:9] + 'i'

        elif(palavras[i][1:9] == 'oulupukk') and len(palavras[i]) == 11:
            palavras[i] = 'J' + palavras[i][1:9] + 'i.'

    print(' '.join(palavras))