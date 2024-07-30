n = input().split()

hi = int(n[0])
hf = int(n[1])

if hi > hf:
    duracao = (hf-hi)-24
    print(f'O JOGO DUROU {abs(duracao)} HORA(S)')
elif (hi==0) and (hf==0):
    print(f'O JOGO DUROU 24 HORA(S)')
else:
    print(f'O JOGO DUROU {abs(hf-hi)} HORA(S)')
