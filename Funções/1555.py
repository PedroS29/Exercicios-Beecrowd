def funcoes(n):
        for i in range(n):
            num = input().split()
            x = int(num[0])
            y = int(num[1])
            rafa = 0; beto = 0; carlos = 0

            rafa += ((3*x)**2 + y**2)
            beto += (2*(x**2) + (5*y)**2)
            carlos += (-100*x + y**3)

            if rafa > beto and rafa > carlos:
                print('Rafael ganhou')
            elif beto > rafa and beto > carlos:
                print('Beto ganhou')
            elif carlos > rafa and carlos > beto:
                print('Carlos ganhou')

funcoes(int(input()))