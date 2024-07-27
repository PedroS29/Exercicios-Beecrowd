linha1 = (input().split())

c1 = linha1[0]
n1 = linha1[1]
v1 = linha1[2]

linha2 = (input().split())

c2 = linha2[0]
n2 = linha2[1]
v2 = linha2[2]

valor = int(n1)*float(v1) + int(n2)*float(v2)

print(f'VALOR A PAGAR: R$ {valor:.2f}')