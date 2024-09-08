x = int(input())
y = int(input())

soma_imp = 0

# if x < y:
#   x, y = y, x

if x <= y:
    x += 1
    while x < y:
        if x%2 != 0:
            soma_imp += x
        x += 1
else:
    y += 1
    while y < x:
        if y%2 != 0:
            soma_imp += y
        y += 1

print(soma_imp)