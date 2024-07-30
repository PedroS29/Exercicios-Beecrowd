n = float(input())

if n > 0 and n <= 400:
    salario = n + (n*0.15)
    reajuste = n*0.15
    percentual = '15 %'
elif n > 400 and n <=800:
    salario = n + (n*0.12)
    reajuste = n*0.12
    percentual = '12 %'
elif n > 800 and n <=1200:
    salario = n + (n*0.10)
    reajuste = n*0.10
    percentual = '10 %'
elif n > 800 and n <=2000:
    salario = n + (n*0.07)
    reajuste = n*0.07
    percentual = '7 %'
else:
    salario = n + (n*0.04)
    reajuste = n*0.04
    percentual = '4 %'

print(f'Novo salario: {salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual}')