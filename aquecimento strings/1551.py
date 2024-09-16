n = int(input())
alfabeto = list('abcdefghijklmnopqrstuvxwyz')
resposta = []

for i in range(n):
    frase = input().split()

    for palavra in range(len(frase)):
        for letra in range(len(alfabeto)):
            if alfabeto[letra] in frase[palavra]:
                if alfabeto[letra] in resposta:
                    continue
                else:
                    resposta.append(alfabeto[letra])

    if len(resposta) == 26:
        print('frase completa')
    elif len(resposta) >= 13 and len(resposta) < 26:
        print('frase quase completa')
    else:
        print('frase mal elaborada')