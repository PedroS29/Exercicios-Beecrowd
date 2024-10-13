#Questão 1
qua_imp = [i*i for i in range(1,10) if i%2!=0]
print(qua_imp)

#Questão 2
lista_sete = [i for i in range(1,108) if '7' in str(i)]
print(lista_sete)

#Questão 3
fraseq3 = input('frase da questão 3: ')
fraseq3_sem_espaco = [i+'1' for i in fraseq3 if i.isspace() == True]
print(len(fraseq3_sem_espaco))

#Questão 4
fraseq4 = input('frase da questão 4: ')
consoantes = [i for i in fraseq4 if i not in 'AaãáEeéIiíOoõóUuú ']
print(consoantes)

#Questão 5
c = list(map(int, input('Digite temperaturas em celsius: ').split()))
fahrenheit = [i * (9/5) + 32 for i in c]
print(fahrenheit)

#Questão 6
numeros = list(map(int, input('Digite uma lista de números: ').split()))
primos = [i for i in numeros if i > 1 and all(i % divisor != 0 for divisor in range(2, int(i**0.5) + 1))]
print(primos)

#Questão 7
string = input('Digite uma string: ') 
string_sem_vogal = ''.join([i for i in string if i not in 'aeiouAEIOU'])
print(string_sem_vogal)

#Questão 8
tabuada = [i*7 for i in range(1,11)]
print(tabuada)

#Questão 9
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
produto = [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print(produto)

#Questão 10
palavras = input('Digite uma lista de palavras: ').split()
palavra_fornecida = input('Digite uma palavra: ')
anagramas = [i for i in palavras if sorted(i) == sorted(palavra_fornecida)]
print(anagramas)

#Questão 11
'''Laço iterativo: No geral, o laço iterativo se destaca por apresentar a melhor legibilidade, ajuda no entendimento em caso de códigos mais extensos
   List comprehension: Por possuir menos linhas de código ela é geralmente processada mais rápida em comparação com o laço iterativo
   Expressões(Funções) geradores: ao produzirem um item por vez e não gerarem toda a sequência de uma só vez como em uma list_comprehension, os geradores possuem melhor performance em questões de eficiência de memória.'''