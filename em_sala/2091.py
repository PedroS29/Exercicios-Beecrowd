n = int(input())

while n != 0:
    linha = list(map(int, input().split()))
    pilha = []
    if n == 0:
        break

    for item in linha:
        if item in pilha:
            pilha.remove(item)
        else:
            pilha.append(item)
    print(pilha[0])
    n = int(input())