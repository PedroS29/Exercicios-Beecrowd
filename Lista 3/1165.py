n = int(input())

i = 1
j = 1
cont = 0
resto = 0

while i <= n:
    x = int(input())
    while j <= x:
        resto = x%j
        if resto == 0:
            cont += 1
        j += 1
    if cont == 2:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')
    i += 1