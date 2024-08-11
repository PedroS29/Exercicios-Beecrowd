turma = 0

while True:
    alunos = int(input())
    if alunos == 0:
        break
    turma += 1
    C = []
    M = []

    for i in range(alunos):
        x = input().split()

        codigo = int(x[0])
        media = int(x[1])

        C.append(codigo)
        M.append(media)

    print(f'Turma {turma}')
    maior_media = max(M)

    for i in range(alunos):
        if M[i] == maior_media:
            print(C[i], end=" ")
    print("\n")