diaI = input().split()
momI = input().split(' : ')

diaF = input().split()
momF = input().split(' : ')

diaI = int(diaI[1])
horaI = int(momI[0])
minutoI = int(momI[1])
segundoI = int(momI[2])

diaF = int(diaF[1])
horaF = int(momF[0])
minutoF = int(momF[1])
segundoF = int(momF[2])

segundo = 0
minuto = 0
hora = 0
dia = 0

if segundoI > segundoF:
    segundo = segundoF + 60 - segundoI
    minutoI += 1
else:
    segundo = segundoF - segundoI

if minutoI > minutoF:
    minuto = minutoF + 60 - minutoI
    horaI += 1
else:
    minuto = minutoF - minutoI

if horaI > horaF:
    hora = horaF + 24 - horaI
    diaI += 1
else:
    hora = horaF - horaI

dia = diaF - diaI
if dia < 0:
    dia += 30
    if hora > 0 or minuto > 0 or segundo > 0:
        dia -= 1

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundo} segundo(s)')