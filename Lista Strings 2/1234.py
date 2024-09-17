n = int(input())

for _ in range(n):
    frase = input().split()
    resposta = []

    for palavra in frase:
        nova_palavra = ''

        for i in range(len(palavra)):
            if i % 2 == 0:
                nova_palavra += palavra[i].upper()
            else:
                nova_palavra += palavra[i]
        resposta.append(nova_palavra)
    print(' '.join(resposta))