# Calcular a média de valores de uma lista

# lista = [10, 2, 3]

# j = 0

# for i in lista:
#     j += i
    
# media = j/len(lista)

# print(media)

def media(lista:list) -> float:
    j = 0
    for i in lista:
        j += i

    return(j/len(lista))

numeros = [10, 2, 3, 25]

avg = media(numeros)
print(avg)
