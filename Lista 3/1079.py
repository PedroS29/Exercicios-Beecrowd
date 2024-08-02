n = int(input())

i = 0

while i < n:
    num = input().split()
    n1 = float(num[0])
    n2 = float(num[1])
    n3 = float(num[2])

    mediap = (n1*2 + n2*3 + n3*5)/10
    print(f'{mediap:.1f}')
    i += 1