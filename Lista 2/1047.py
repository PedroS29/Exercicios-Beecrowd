n = input().split()

hi = int(n[0])
mi = int(n[1])
hf = int(n[2])
mf = int(n[3])

inicio = hi * 60 + mi
fim = hf * 60 + mf

if fim <= inicio:
    fim += 24 * 60

duracao_minutos = fim - inicio
horas = duracao_minutos // 60
minutos = duracao_minutos % 60

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')