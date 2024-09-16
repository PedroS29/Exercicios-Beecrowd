n = int(input())

for i in range(n):
    A, B = map(str, input().split())

    tam = len(B)

    if tam > len(A):
        print('nao encaixa')
    elif A[-tam:] != B:
        print('nao encaixa')
    else:
        print('encaixa')