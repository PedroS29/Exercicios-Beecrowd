n = int(input())

for i in range(n):
    string = input()

    pri = int(string[2:4])
    seg = int(string[5:8])
    ter = int(string[11:13])

    soma = pri+seg+ter
    print(soma)