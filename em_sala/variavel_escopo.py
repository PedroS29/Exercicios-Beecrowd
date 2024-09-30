x = 5
#Definição da função ou assinatura
def altera_valor():
    #global x
    x = 7
    print(f'O valor de x dentro da função: {x}')
#Programa Principal
print(f'O valor de x fora da função: {x}')
altera_valor() #Chamada da função
print(f'O valor de x após a chamada da função: {x}')