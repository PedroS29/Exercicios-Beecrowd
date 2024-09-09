n = int(input())

for i in range(n):
    leds = 0

    teste = list(input())

    for i in teste:
        if i == '1':
            leds += 2
        elif i == '2' or i == '3' or i == '5':
            leds += 5
        elif i == '4':
            leds += 4
        elif i == '6' or i == '9' or i == '0':
            leds += 6
        elif i == '7':
            leds += 3
        elif i == '8':
            leds += 7

    print(f'{leds} leds')