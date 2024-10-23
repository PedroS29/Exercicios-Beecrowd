import sys

while True:
    try:
        entrada = input('Entre com um número: ')
        valor = int(entrada)
        if valor < 0:
            raise ValueError('Não quero valores negativos')
        x = 5 / valor
        print(x)
    except ValueError as erro:
        print(str(erro))
        # print(erro.__str__)
        print('Tente novamente...')
        #print(f'{sys.exc_info()}')
    except ZeroDivisionError as zde:
        print('Não é possível fazer divisão por zero.')
        raise
    except EOFError as eor:
        print('Fim do programa.')
        break
    else:
        print(f'O resultado de 5 / {entrada} = {x}')
    finally:
        print(f'A entrada foi {entrada}.')