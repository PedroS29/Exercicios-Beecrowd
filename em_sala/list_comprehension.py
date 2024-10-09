num = [1,2,3,4,5,6,7,8,9,10]
#Nova lista com elementos ao quadrado
quadrados = [item*item for item in num ]
print(quadrados)

#Lista apenas com os números pares
pares = [i for i in num if i % 2 == 0]
print(pares)

#Lista com pares e quadrados impares
lista = [i if i%2 == 0 else i*i for i in num]
print(lista)

letras = ['a','b','c']
#Lista que combina todas as letras com os números
combina = [(letra, n)for letra in letras for n in num]
print(combina)

#Lista que combina todos os números com as letras
combina2 = [(letra, n) for n in num for letra in letras]
print(combina2)

combina3 = [[letra, n] for n in num for letra in letras]
print(combina3)

#Uma matriz de 3 linhas e 4 colunas
matriz = [[j+1+i*4 for j in range(4)] for i in range(3)]
print(matriz)

transposta = []

#Modo iterativo
for j in range(4):
    linha = []
    for i in range(3):
        linha.append(matriz[i][j])
    transposta.append(linha)
print(transposta)

#Modo list-comprehension
transposta2 = [[matriz[i][j] for i in range(3)]for j in range(4)]
print(transposta2)

#Usando strings
frutas = [' abacate', ' banana ', 'abacaxi ']
novas_frutas = [fruta.strip().upper() for fruta in frutas]
print(novas_frutas)

#Usando set
frase = 'Exemplo de set comprehension'

vogais = [i for i in frase if i in 'aeiou']
vogais_unicas = {i for i in frase if i in 'Eaeiou'}

print(vogais)
print(vogais_unicas)

#Usando dicionário
vogais_dict = {i:i.upper() for i in frase if i in 'aeiou'}
print(vogais_dict)
