lista = [1, 5, 7, 9, 15, 27, 32, 14, 12, 21]
listaAlterada = []
i = 0

def AcrescentarValor():
    global i
    valor = lista[i]
    print('Digite o valor que deseja inserir: ', valor)
    if valor in listaAlterada:
        print('Valor', valor, 'não pode ser adicionado a lista!\n')
    else:
        listaAlterada.append(valor)
        print('Valor', valor, 'adicionado com sucesso!\n')
    i += 1


def RemoverValor():
    global i
    i -= 1
    valor = lista[i]
    valor -= 1
    print('Digite o valor que deseja remover: ', valor)
    while valor not in listaAlterada:
        print(valor, 'não está na lista!\n')
        valor -= 1
        print('Digite o valor que deseja remover: ', valor)
    if valor in listaAlterada:
        listaAlterada.remove(valor)
        print('Valor', valor, 'removido com sucesso!\n')
    else:
        print('Valor não está na lista!\n')


def VerificarLista():
    print('Lista atual: ')
    for x in listaAlterada:
        print(x, end=' ')
    print('\n')


AcrescentarValor()
AcrescentarValor()
AcrescentarValor()
AcrescentarValor()
AcrescentarValor()

VerificarLista()

RemoverValor()
RemoverValor()
RemoverValor()

VerificarLista()
