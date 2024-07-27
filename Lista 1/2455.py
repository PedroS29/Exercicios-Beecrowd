n = input().split()

p1 = int(n[0])
c1 = int(n[1])
p2 = int(n[2])
c2 = int(n[3])

calc1 = (p1)*(c1)
calc2 = (p2)*(c2)

if calc1 == calc2:
    print('0')
elif calc1 > calc2:
    print('- 1')
else:
    print('1')