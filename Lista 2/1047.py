n = input().split()

hi = int(n[0])
mi = int(n[1])
hf = int(n[2])
mf = int(n[3])


if hi > hf:
    print(f'O JOGO DUROU {abs((hi-hf)-24)} HORA(S)')
elif (hi==0) and (hf==0):
    print(f'O JOGO DUROU 24 HORA(S)')
else:
    print(f'O JOGO DUROU {abs(hf-hi)} HORA(S)')
