n = int(input())

hora = 0
min = 0

while n > 59:
    min += 1
    if min > 59:
        hora += 1
        min -= 60
    n -= 60

print(f'{hora}:{min}:{n}')