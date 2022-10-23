from sympy import false


def executar_busca_binaria(lista, valor,):

    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        #encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        #VERIFICA SE O VALOR PROCURADO ESTA A ESQUERDA OU A DIREITA DO VALOR CENTRAL
        if valor < lista[meio]:
            maximo = meio - 1

        elif valor > lista[meio]:
            minimo = meio + 1
    else:
        return false

lista = list(range(1, 50))

print(lista)

print('\n', executar_busca_binaria(lista=lista, valor = 7))
print('\n', executar_busca_binaria(lista=lista, valor = 7))



