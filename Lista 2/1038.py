n = input().split()

cod = int(n[0])
qtd = int(n[1])

if cod == 1:
    print(f'Total: R$ {qtd*4:.2f}')
elif cod == 2:
    print(f'Total: R$ {qtd*4.5:.2f}')
elif cod == 3:
    print(f'Total: R$ {qtd*5:.2f}')
elif cod == 4:
    print(f'Total: R$ {qtd*2:.2f}')
else:
    print(f'Total: R$ {qtd*1.5:.2f}')