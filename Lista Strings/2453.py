frase = input().split()
resposta = []

for palavra in frase:
    resposta.append(palavra[1::2])

for i in range(len(resposta)):
    if i == len(resposta)-1:
        print(resposta[i])
    else:
        print(resposta[i], end=' ')