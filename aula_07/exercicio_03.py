# Contar valores únicos de uma lista

# lista: list = [1, 1, 2, 3, 4, 4, 5, 5, 5, 5, 6]

# lista_valores_unicos : list = []

# for i in lista:
#     if i in lista_valores_unicos:
#         pass
#     else:
#         lista_valores_unicos.append(i)

# print(len(lista_valores_unicos))

def valores_unicos(lista: list) -> int:
    lista_valores_unicos =[]

    for i in lista:
        if i in lista_valores_unicos:
            pass
        else:
            lista_valores_unicos.append(i)

    return len(lista_valores_unicos)

lista: list = [1, 1, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 7, 8, 111]

contagem_valores_unicos = valores_unicos(lista)

print(contagem_valores_unicos)