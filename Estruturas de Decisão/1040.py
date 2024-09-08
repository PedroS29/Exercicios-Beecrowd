n = input().split()

n1 = float(n[0])
n2 = float(n[1])
n3 = float(n[2])
n4 = float(n[3])

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10

print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota = float(input())
    print(f'Nota do exame: {nota:.1f}')

    media2 = (media+nota)/2
    if media2 >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {media2:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {media2:.1f}')