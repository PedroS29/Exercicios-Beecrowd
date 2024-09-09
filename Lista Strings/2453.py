palavras = input()

frase = palavras.split()

for palavra in frase:
    if frase.index('p')%2 == 0:
        palavra.replace('p')

print(frase)