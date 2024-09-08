n = input().split()

a = float(n[0])
b = float(n[1])
c = float(n[2])

if (a >= b + c) or (b >= a + c) or (c >= b + a):
    print('NAO FORMA TRIANGULO')
else:
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a:
        print('TRIANGULO RETANGULO')
    elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > b*b + a*a:
        print('TRIANGULO OBTUSANGULO')
    elif a*a < b*b + c*c or b*b < a*a + c*c or c*c < b*b + a*a:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')