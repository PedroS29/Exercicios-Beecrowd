'''1)Escreva um programa que receba duas listas com nomes de pessoas e determine:

● Quantas pessoas estão nas duas listas ao mesmo
tempo
● Quantas pessoas duplicadas
● O total de pessoas distintas nas duas listas
● Quantas pessoas estão apenas em uma das duas listas'''

a = input('Entre com a primeira lista: ')
aset= set(a)
b = input('Entre com a segunda lista: ')
bset= set(b)

print(f'Total de pessoas presentes nas duas listas ao mesmo tempo: {len(aset & bset)}')

print(f'Total de pessoas duplicadas na lista 1 e 2, respectivamente: {len(a)-len(aset)} e {len(b)-len(bset)}')

print(f'Total de pessoas distintas nas duas listas: {len(aset ^ bset)}')

print(f'Total de pessoas presentes em apenas uma das duas listas: {len(aset ^ bset)}')