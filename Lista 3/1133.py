n1 = int(input())
n2 = int(input())

if n1 > n2:
    n1,n2 = n2,n1

n1 += 1

while n1 < n2:
    if n1%5 == 2 or n1%5 == 3:
        print(n1)
    n1 += 1