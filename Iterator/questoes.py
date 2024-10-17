#questao1
ger = (list((i,i+2) for i in range(6) if i!=3))
print(f'Resultado da questão 1: {ger}\n')

#questao2
# ger = 

#questao3
import random
ger3 = (list(random.randint(1,60) for _ in range(6)))
print(f'Resultado da questão 3: {ger3}')

#questao4
# entrada = int(input('Insira os valores em tuplas: '))
# ger4 = (sum(i) for i in entrada)
# for i in ger4:
#     print(i)

#questao5
# entrada2 = iter(input('Insira os elementos: '))
# for i in entrada2:
#     if i != i:


#questao6
'''Em questão de velocidade a segunda função é preferível
por se tratar de uma list_comprehension onde a lista 
resultante da expressão é gerada toda de uma vez, em 
questão de economia de memória a primeira função é 
preferível já que se trata de uma generator expression 
onde os itens são gerados um de cada vez.'''