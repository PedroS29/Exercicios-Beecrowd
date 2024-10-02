def paula(n):
    for i in range(n):
        digitos = list(input())
        if digitos[1].isupper() == True:
            if digitos[0] == digitos[2]:
                print(int(digitos[0])*int(digitos[2]))
                continue
            print(int(digitos[2])-int(digitos[0]))
        else:
            if digitos[0] == digitos[2]:
                print(int(digitos[0])*int(digitos[2]))
                continue
            print(int(digitos[0])+int(digitos[2]))

paula(int(input()))