total = int(input())
compradas = int(input())

figurinhas_compradas = []

for _ in range(compradas):
    figurinhas_compradas.append(int(input()))

figurinhas_unicas = []

for figurinha in figurinhas_compradas:
    if figurinha not in figurinhas_unicas:
        figurinhas_unicas.append(figurinha)

faltando = total - len(figurinhas_unicas)

print(faltando)