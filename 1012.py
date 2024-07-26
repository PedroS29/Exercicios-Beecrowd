z = input().split()

A = (z[0])
B = (z[1])
C = (z[2])

area_tri = float(A)*float(C)/2
area_cir = (float(C)*float(C))*3.14159
area_tra = ((float(A)+float(B))*float(C))/2
area_qua = float(B)*float(B)
area_ret = float(A)*float(B)

print(f'TRIANGULO: {area_tri:.3f}')
print(f'CIRCULO: {area_cir:.3f}')
print(f'TRAPEZIO: {area_tra:.3f}')
print(f'QUADRADO: {area_qua:.3f}')
print(f'RETANGULO: {area_ret:.3f}')