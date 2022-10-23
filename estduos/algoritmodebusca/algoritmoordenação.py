'''lista = [30, 4, 1, 15, -3]

lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()

print('lista = ', lista, '\n')
print('lista_ordenada1 = ', lista_ordenada1)
print('lista_ordenada2 = ', lista_ordenada2)
print('lista =', lista)

lista = [7, 5]

if lista [0] > lista [1]:
    aux = lista[1]
    lista[1]= lista[0]
    lista[0] = aux


print(lista)'''


def executar_selection_sort(lista):
    n = len(lista)
    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista [j] < lista [index_menor]:
                index_menor = j
            lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

lista = [10, 9, 5, 8, 11, 1, 3]
print(executar_selection_sort(lista))

