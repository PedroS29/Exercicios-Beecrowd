'''3. Crie um programa que solicite ao usuário uma lista de valores inteiros separados por vírgulas. Divida a
String em valores individuais, convertendo cada String em um número inteiro. Você deve usar uma
instrução try/except para informar ao usuário quando os valores inseridos não podem ser convertidos.'''

while True:
    try:
        n = list(map(int, input('Insira uma lista de valores inteiros separados por vírgulas: ').split(',')))
    except ValueError:
        print('Os valores inseridos não podem ser convertidos.')
    else:
        print(f'Os valores recebidos foram: {n}')
        break