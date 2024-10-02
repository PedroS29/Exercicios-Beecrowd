def livro(p):
    total = 0
    for i in range(1,p+1):
        total += len(str(i))
    print(total)

livro(int(input()))