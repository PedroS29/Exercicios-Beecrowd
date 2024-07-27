L = input()

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = 1
i = 0

while i < 26:
    if alfabeto[i] == L:
        print(n)
    n += 1
    i += 1