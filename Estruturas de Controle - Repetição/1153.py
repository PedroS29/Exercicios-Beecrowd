n = int(input())

i = n-1

while i > 1:
    n *= i
    i -= 1
print(n)