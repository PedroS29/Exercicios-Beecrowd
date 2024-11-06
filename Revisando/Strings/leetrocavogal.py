palavra = input('Entre com uma palavra: ')

resultado = ''.join(['*' if letra.lower() in 'aeiou' else letra for letra in palavra])

# resultado = ''

# for letra in list(palavra):
#     if letra.lower() in 'aeiou':
#         resultado += '*'
#     else:
#         resultado += letra

print(f'Palavra sem vogais: {resultado}')