n = input().split()

A = float(n[0])
B = float(n[1])
C = float(n[2])

delta = (B*B) - (4*A*C)

if A == 0:
    print('Impossivel calcular')
else:
    if delta < 0:
        print('Impossivel calcular')
    else:
        R1 = (-B + (delta ** 0.5)) / (2 * A)
        R2 = (-B - (delta ** 0.5)) / (2 * A)

        print(f'R1 = {R1:.5f}')
        print(f'R2 = {R2:.5f}')