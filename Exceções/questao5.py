'''5. Crie uma função que recebe um String como parâmetro e verifica se a mesma é composta apenas por
caracteres maiúsculos. A função deve lançar dois tipos de exceções: uma para indicar se existe algum
caractere que não é uma letra e a outra para indicar se algum dos caracteres não é maiúsculo.'''

class NaoLetra(Exception):
    pass
class Minusculo(Exception):
    pass

def maiuscula():
    while True:
        try:
            string = input('Insira uma string: ')
            for i in string:
                if i.isalpha() == False:
                    raise NaoLetra(f'Caractere diferente de letra detectado: {i}')
                elif i.islower() == True:
                    raise Minusculo(f'Há um caractere minúsculo entre os inseridos: {i}')
                
        except NaoLetra as nl:
            print(nl)
        except Minusculo as m:
            print(m)
        else:
            print('String composta apenas por caracteres maiúsculos!')

maiuscula()