n = int(input())
resposta = ''

for i in range(n):
    palavra1, palavra2 = map(str, input().split())

    tamanho = min(len(palavra1), len(palavra2))

    for j in range(tamanho):
        resposta += palavra1[j] + palavra2[j]
    
    if tamanho == len(palavra2):
        resposta += palavra1[tamanho:]
    else:
        resposta += palavra2[tamanho:]
    print(resposta)
    resposta = ''