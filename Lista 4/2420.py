seções = int(input())
territorio = [0]*seções

x = input().split()
for i in range(seções):
    territorio[i] = int(x[i])

total = sum(territorio)
lado_esq = 0

for i in range(seções):
    lado_esq += territorio[i]
    lado_dir = total - lado_esq

    if lado_esq == lado_dir:
        print(i + 1)
        break