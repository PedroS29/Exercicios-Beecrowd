def binario(n):
    for i in range(n):
        uns = 0
        num = int(input())
        num_bin = bin(num)

        for i in range(len(num_bin)):
            if num_bin[i] == '1':
                uns += 1
        print(uns)

binario(int(input()))