#questao1
ger = (list((i,i+2) for i in range(6) if i!=3))
print(f'Resultado da questão 1: {ger}\n')

#questao2
def ger2():
    i = 0
    while True:
        yield i
        i += 1

#questao3
import random
ger3 = (list(random.randint(1,60) for _ in range(6)))
print(f'Resultado da questão 3: {ger3}')

#questao4
entrada = [(1, 2, 3), (5, 7), (99, 15, -5)]
ger4 = (sum(i) for i in entrada)
lista = []
for i in ger4:
    lista.append(i)
print(*lista)

#questao5

#questao6
'''Em questão de velocidade a segunda função é preferível
por se tratar de uma list_comprehension onde a lista 
resultante da expressão é gerada toda de uma vez, em 
questão de economia de memória a primeira função é 
preferível já que se trata de uma generator expression 
onde os itens são gerados um de cada vez.'''