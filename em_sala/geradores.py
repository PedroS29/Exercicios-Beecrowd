# Criar um iterador
iterador = iter('ABC')
# Qualquer iterável pode ser percorrido com laço
for i in iterador:
    print(i)
# A função next só funciona em iterators
# print(next(iterador), next(iterador), next(iterador))
# Não podemos usar next em iteráveis
# Função que retorna iterador
alunos = ['Alice', 'Bernando', 'Carlos']
alunos_iterator = enumerate(alunos) # o retorno é um iterador
# print(next(it))
for i in alunos_iterator:
    print(i)
reverso = reversed(alunos) # iterador que começa do último elemento
for i in reverso:
    print(i)
# Criar um dicionário a partir de um 
# Precisamos reiniciar o iterador
it = enumerate(alunos)
dicionario = dict(it)
print(dicionario)
for i in it:
    print(i)

numeros = [1,2,3,4]
geradora = (n**2 for n in numeros)
combinacao = zip(numeros, geradora) # Sempre percorrerá até o tamanho da menor coleção

for i in combinacao:
    print(i)

def imprimir():
    print('Imprime 1')
    yield 1
    print('Imprime 2')
    yield 2
    print('Imprime 3')
    yield 3

it = imprimir() #O retorno da função geradora é um iterador
print(it)
print(next(it), next(it), next(it))

def geradora():
    for i in range(10):
        yield i

it = geradora()

while True:
    try:
        print(print(next(it)))
    except StopIteration:
        break