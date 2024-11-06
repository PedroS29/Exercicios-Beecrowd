# Lista de faturas
fatura = [('Net', 199.9), ('Ifood', 999.87), ('Gasolina', 678.0), ('Formigão', 400)]

# 1. Imprimir no formato 'Tipo de gasto – R$ valor'
print("Fatura detalhada:")
for item in fatura:
    print(f"{item[0]} – R$ {item[1]:.2f}")

# 2. Ordenar os itens por valor
fatura_ordenada = sorted(fatura, key=lambda x: x[1], reverse=True)
print("\nFatura ordenada por valor (decrescente):")
for item in fatura_ordenada:
    print(f"{item[0]} – R$ {item[1]:.2f}")

# 3. Filtrar os gastos acima de R$ 500
fatura_acima_500 = [item for item in fatura if item[1] > 500]
print("\nGastos acima de R$ 500:")
for item in fatura_acima_500:
    print(f"{item[0]} – R$ {item[1]:.2f}")

# 4. Apresentar o total da fatura
total_fatura = sum(item[1] for item in fatura)
print(f"\nTotal da fatura: R$ {total_fatura:.2f}")
