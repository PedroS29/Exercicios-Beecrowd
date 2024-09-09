maior_palavra = ""

while True:
    palavra = input()

    if palavra == '0':
        print(f'The biggest word: {maior_palavra}')
        break

    frase = palavra.split()

    for item in frase:
        if len(item) >= len(maior_palavra):
            maior_palavra = item

    for item in frase[:-1]:
        print(f'{len(item)}-', end='')
    print(f'{len(frase[-1])}')