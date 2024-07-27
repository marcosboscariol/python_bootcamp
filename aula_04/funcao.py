# lista_de_numeros = [100, 50, 60]

# lista_de_numeros.sort()


def ordenar_lista_de_numeros(numeros):
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i+1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]

    return print(nova_lista_de_numeros)


# ordenar_lista_de_numeros(lista_de_numeros)

# lista_de_numeros.sort()

# print(lista_de_numeros)
