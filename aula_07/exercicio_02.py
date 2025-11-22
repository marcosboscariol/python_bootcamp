# Filtrar dados acima de um limite

def filtrar(lista: list, limite: float) -> list:
    lista_final = []
    for i in lista:
        if i > limite:
            lista_final.append(i)

    return(lista_final)

numeros: list = [1, 2, 3, 4, 5]
limite: float = 3.0

valor_final = filtrar(numeros, limite)
print(valor_final)