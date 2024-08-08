i = 1
notas = 0.0

while i <= 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        i = i + 1
        notas += nota

media = notas/2

print(f'media = {media:.2f}')