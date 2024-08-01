n = int(input())

i = 1
d = 0
f = 0

while i <= n:
    x = int(input())
    if x >= 10 and x <= 20:
        d += 1
    else:
        f += 1
    i += 1

print(f'{d} in')
print(f'{f} out')