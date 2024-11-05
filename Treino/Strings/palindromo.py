x = input('Escreva uma palavra: ')

palindromo = [print('É um palíndromo') if x[::] == x[::-1] else print('Não é um palíndromo')]


# if x[::] == x[::-1]:
#     print(f'A palavra {x} é um palíndromo')
# else:
#     print(f'A palavra {x} não é um palíndromo')