n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])

if a < b < c:
    print(a)
    print(b)
    print(c)
elif b < a < c:
    print(b)
    print(a)
    print(c)
elif c < a < b:
    print(c)
    print(a)
    print(b)
elif a < c < b:
    print(a)
    print(c)
    print(b)
elif b < c < a:
    print(b)
    print(c)
    print(a)
else:
    print(c)
    print(b)
    print(a)

print()
print(a)
print(b)
print(c)