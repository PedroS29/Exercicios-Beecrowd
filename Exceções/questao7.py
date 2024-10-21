'''7. Crie um programa que solicitará uma confirmação: sim ou não, que deverá ser impressa. Considere que
os usuários podem inserir quaisquer valores, você precisa garantir que as diferentes possibilidades sejam
tratadas corretamente. Se uma resposta desconhecida for fornecida, o programa deve gerar uma exceção
personalizada chamada RespostaInvalidaError e forçar que o usuário forneça um valor válido.'''

class RespostaInvalidaError(Exception):
    pass

while True:
    try:
        n = input('Confirme sua resposta: sim/não\n')
        if n != 'sim' and n != 'não':
            raise RespostaInvalidaError('Resposta inválida. Tente Novamente...')
        else:
            print(f'Resposta recebida: {n}!')
            break
    except RespostaInvalidaError as rie:
        print(rie)