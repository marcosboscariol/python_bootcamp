# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

'''
lista = []
lista_quadrada = []

for n in range(1, 11):
    lista.append(n)

print(lista)

for n in lista:
    lista_quadrada.append(n ** 2)

print(lista_quadrada)
'''

# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

'''
lista = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.insert(1, "Ruby")

print(lista)
'''

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

'''
livro = {
    'titulo': 'Título do Livro',
    'autor': 'Autor do Livro',
    'ano_publicacao': 2000
}

for n in livro:
    print(n, livro[n])
'''

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

'''
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))
'''

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

'''
lista = ["maçã", "banana", "cereja"]

dicionario = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

preco = 0

for preco_fruta in dicionario:
    preco += dicionario[preco_fruta]

print(preco)
'''
