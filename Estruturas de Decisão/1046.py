n = input().split()

hi = int(n[0])
hf = int(n[1])

if hi > hf:
    print(f'O JOGO DUROU {abs((hi-hf)-24)} HORA(S)')
elif hi==hf:
    print(f'O JOGO DUROU 24 HORA(S)')
else:
    print(f'O JOGO DUROU {abs(hf-hi)} HORA(S)')
