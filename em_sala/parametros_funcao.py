def fat(n):
    #fatorial = 0
    #if n == 0:
    #    return 1
    #else:
    #    fatorial = n * fat(n-1)
    #return fatorial

    #forma imperativa
    fatorial2 = 1
    while n > 0:
        fatorial2 *= n-1
        n -= 1
    return fatorial2
    
def fib(n):
    if 1 <= n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

    
#Parâmetros: uma função e um inteiro    
def soma(funcao, inteiro):
    total = 0
    for i in range(1,inteiro+1):
        total += funcao(i)
    return total

#Programa principal
print(soma(fat,3))
print(soma(fib,3))