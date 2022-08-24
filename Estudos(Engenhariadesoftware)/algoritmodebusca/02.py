def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

import random

lista = random.sample(range(100), 20)
print(sorted(lista))
print(executar_busca_linear(lista, 10))