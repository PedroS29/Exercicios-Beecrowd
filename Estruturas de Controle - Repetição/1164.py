n = int(input())

i = 1
resto = 0

while i <= n:
    x  = int(input())
    j = 1
    div = 0
    while j < x:
        resto = x%j
        if resto == 0:
            div += j
        j += 1
    if div == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')
    i += 1
