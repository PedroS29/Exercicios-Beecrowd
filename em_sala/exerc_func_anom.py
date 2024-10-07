from functools import reduce

Fatura = [('Net', 199.9),('Ifood', 999.87),('Gasolina', 678.0),('Formigão', 400)]

#Imprimir no formato 'Tipo de gasto' - R$ valor
print(list(map(lambda x: f'Tipo gasto: {x[0]} R$ valor: {x[1]}', Fatura)))

#Ordenar os itens por valor
Fatura.sort(key = lambda x: x[1])
print(Fatura)

#Filtrar os gastos acima de R$ 500
Fatura2 = list(filter(lambda x : x[1] > 500, Fatura))
print(Fatura2)

#Apresentar o total da fatura
Total = list(map(lambda x: x[1], Fatura))
print(sum(Total))
