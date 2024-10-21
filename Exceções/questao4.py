'''4. Escreva um programa que leia um valor real do teclado armazenando-o em uma variável do tipo float. Se
o usuário digitar um valor que não possa ser convertido em um valor do tipo float, seu programa deve
solicitar ao usuário que digite um novo valor. Se o usuário não digitar um valor aceitável por três vezes, seu
programa deve terminar imprimindo a mensagem “Você excedeu o limite de tentativas.”.'''
i = 0

while True:
    if i == 3:
        print('Você excedeu o limite de tentativas.')
        break

    try:
        n = float(input('Insira um valor real: '))
    except ValueError:
        i += 1
        print('O valor inserido não pode ser convertido. Repita a inserção de dados.')