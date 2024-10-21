'''6. Crie uma exceção chamada FahrenheitError. Desenvolva uma função para converter temperaturas em
graus Fahrenheit para graus Celsius, ambas representadas em ponto flutuante (float). Porém, caso o valor a
ser convertido seja menor que zero absoluto (-459,67°F) deve-se lançar a exceção FahrenheitError. A
fórmula para conversão é dada por: C = 5 (F − 32) / 9'''

class FahrenheitError(Exception):
    pass

def conversor():
    while True:
        try:
            x = float(input('Insira uma temperatura em Fahrenheit: '))
            if x < -459.67:
                raise FahrenheitError('Um valor menor que zero absoluto não pode ser convertido.')
                
            conversao = 5*(x-32)/9
            
        except FahrenheitError as fe:
            print(fe)

        except ValueError:
            print('O valor inserido não pode ser convertido.')

        else:
            print(f'Valor convertido para Celsius: {conversao:.2f}')
            break

conversor()