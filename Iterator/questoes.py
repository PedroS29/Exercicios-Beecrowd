#questao1
def ger():
    for i in range(6):
        if i != 3:
            x = (i, i+2)
            yield x

g1 = ger()
lista = list(g1)
print(f'Resposta da Questão 1:\n{lista}')

#questao2
def ger2():
    i = 0
    while True:
        yield i
        i += 1

#questao3
import random
def ger3():
    i = 0
    for i in range(6):
        i = random.randint(1,60)
        yield i
g3 = ger3()
print(f'Resposta da Questão 3:\n{next(g3),next(g3),next(g3),next(g3),next(g3),next(g3)}')

#questao4
entrada = [(1, 2, 3), (5, 7), (99, 15, -5)]
ger4 = (sum(i) for i in entrada)
listaQ4 = []
for i in ger4:
    listaQ4.append(i)
print('Resposta da Questão 4: ')
print(*listaQ4)

#questao5
def ger5(x):
    x = list(x)
    prox = x[3]
    for i in x:
        if i != prox:
            yield i
        prox = i

g5 = ger5('aaabbacabbbd')
listaQ5 = list(g5)
print(f'Resposta da Questão 5:\n{listaQ5}')

#questao6
'''Em questão de velocidade a segunda função é preferível
por se tratar de uma list_comprehension onde a lista 
resultante da expressão é gerada toda de uma vez, em 
questão de economia de memória a primeira função é 
preferível já que se trata de uma generator expression 
onde os itens são gerados um de cada vez.'''