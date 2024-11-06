def contar_vogais():
    texto = input("Digite um texto para contar as vogais: ")
    vogais = 'aeiou'
    dicionario_vogais = {vogal: texto.lower().count(vogal) for vogal in vogais if texto.lower().count(vogal) > 0}
    return dicionario_vogais

# Exemplo de uso
resultado = contar_vogais()
print("Quantidade de vogais no texto:", resultado)
