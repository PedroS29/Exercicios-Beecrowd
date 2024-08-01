i = 1
par = 0

while i <= 5:
    n = int(input())
    if n%2 == 0:
        par = par + 1
    i = i + 1
print(f'{par} valores pares')