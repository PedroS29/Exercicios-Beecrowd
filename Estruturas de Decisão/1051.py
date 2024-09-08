n = float(input())

if n >= 0 and n <= 2000:
    imposto = 'Isento'
    print(imposto)

elif n > 2000 and n <=3000:
    imposto = (n-2000)*0.08
    print(f'R$ {imposto:.2f}')

elif n > 3000 and n <=4500:
    imposto = 1000*0.08 + (n-3000)*0.18
    print(f'R$ {imposto:.2f}')

else:
    imposto = 1000*0.08 + (1500)*0.18 + (n-4500)*0.28
    print(f'R$ {imposto:.2f}')