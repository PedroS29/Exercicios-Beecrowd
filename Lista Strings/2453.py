palavras = input()

frase_normal = []

for i in range(len(palavras)):
    if palavras[i] == 'p' and palavras[i + 1].isalpha():
        continue
    else:
        frase_normal.append(palavras[i])
    
print("".join(frase_normal))