n = input().split()

a = float(n[0])
b = float(n[1])
c = float(n[2])

if (a < b + c) and (b < a + c) and (c < b + a):
    print(f'Perimetro = {a+b+c:.1f}')
else:
    print(f'Area = {((a+b)*c)/2:.1f}')