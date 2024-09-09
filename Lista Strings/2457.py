letra = input()
frase = input().split()

porcentagem = 0

for palavra in frase:
    if letra in palavra:
        porcentagem = porcentagem + 1

resultado = porcentagem/len(frase)

print(f'{resultado*100:.1f}')