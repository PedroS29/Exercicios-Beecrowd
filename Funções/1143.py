def quadrado(n):
    x = 0
    for i in range(n):
        x += 1
        print(f'{x} {x*x} {x*x*x}')

quadrado(int(input()))