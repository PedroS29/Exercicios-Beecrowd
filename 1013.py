n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])

maiorAB = (a+b+abs(a-b))/2

maiorC = (maiorAB+c+abs(maiorAB-c))/2

print(f'{maiorC:.0f} eh o maior')