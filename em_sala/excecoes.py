def hierarquia(classe, ind=0):
        print('-' * ind, classe.__name__)
        for i in classe.__subclasses__():
                hierarquia(i, ind + 3)

print('A hierarquia de exceções python: ')
hierarquia(Exception)