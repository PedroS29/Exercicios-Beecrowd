n = input().split()

a = float(n[0])
b = float(n[1])
c = float(n[2])

if (a < b + c) and (b < a + c) and (c < b + a):
    if a*a == b*b + c*c:
        print('TRIANGULO RETANGULO')
    elif a*a > b*b + c*c:
        print('TRIANGULO OBTUSANGULO')
    elif a*a < b*b + c*c:
        print('TRIANGULO ACUTANGULO')
    elif a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
