lista_de_numeros: list = [40, 50, 60, 70, 0, -408593, 1, 50]


def ordenar_lista_de_numeros(lista_de_numeros: list) -> list:
    for i in range(len(lista_de_numeros)):
        for j in range(i+1, len(lista_de_numeros)):
            if lista_de_numeros[i] > lista_de_numeros[j]:
                lista_de_numeros[i], lista_de_numeros[j] = lista_de_numeros[j], lista_de_numeros[i]

    return (lista_de_numeros)


lista_ordenada = ordenar_lista_de_numeros(lista_de_numeros)

print(lista_ordenada)

print(sorted(lista_de_numeros))
