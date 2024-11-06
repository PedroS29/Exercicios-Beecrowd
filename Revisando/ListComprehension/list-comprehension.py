# Criar uma lista dos quadrados de todos os números ímpares entre 1 e 10:
quadrados_impares = [x**2 for x in range(1, 11) if x % 2 != 0]
print(quadrados_impares)

# Listar todos os números de 1 a 107 que tenham o dígito 7:
numeros_com_7 = [x for x in range(1, 108) if '7' in str(x)]
print(numeros_com_7)

# Contar o número de espaços em branco de uma frase:
frase = input("Digite uma frase: ")
num_espacos = len([char for char in frase if char == ' '])
print(num_espacos)

# Criar uma lista de todas as consoantes de uma frase:
frase = input("Digite uma frase: ")
consoantes = [char for char in frase if char.lower() in 'bcdfghjklmnpqrstvwxyz']
print(consoantes)

# Converter uma lista de temperaturas em graus Celsius para Fahrenheit:
celsius = [0, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)

# Filtrar todos os números primos de uma lista de números:
numeros = range(1, 50)
primos = [n for n in numeros if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
print(primos)

# Remover todas as vogais de uma string:
string = input("Digite uma string: ")
sem_vogais = ''.join([char for char in string if char.lower() not in 'aeiou'])
print(sem_vogais)

# Criar a tabuada do 7:
tabuada_7 = [7 * i for i in range(1, 11)]
print(tabuada_7)

# Calcular o produto de duas matrizes 2x2:
matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]
produto = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matriz_b)] for row in matriz_a]
print(produto)

# Criar uma lista contendo apenas as palavras que são anagramas de uma palavra fornecida:
palavra = input("Digite a palavra base: ")
lista_palavras = ["amor", "roma", "carro", "mora", "mar"]
anagramas = [p for p in lista_palavras if sorted(p) == sorted(palavra)]
print(anagramas)
