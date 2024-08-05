n = int(input())

i = 1
resto = 0

while i <= n:
    x = int(input())
    aux = 0
    j = 1
    while j <= x:
        resto = x%j
        if resto == 0:
            aux += 1
        j += 1
    if aux == 2:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')
    i += 1