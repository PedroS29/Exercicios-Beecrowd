n = int(input())

ant1 = 0
ant2 = 1

i = 1

print(ant1,ant2, end=' ')

while i <= n-2:
    if i == n-2:
        prox = ant1 + ant2
        print(prox)
    else:
        prox = ant1 + ant2
        print(prox, end=' ')
        ant1 = ant2
        ant2 = prox
    i += 1