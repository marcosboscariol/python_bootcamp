# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

"""
lista = []

for n in range (1,11):
    lista.append(n)


for n in lista:
    numero = n ** 2
    print(f"{n} ao quedraro = {numero}")
"""

# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

"""
lista = ["Python", "Java", "C++", "JavaScript"]
print (lista)

lista.remove("C++")

lista.append("Ruby")

print(lista)
"""

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

"""
dicionario = {
    "Título": "Título do livro",
    "Autor": "Autor do livro",
    "Ano": 2024
}

for n,m in enumerate (dicionario):
    print(f"{m}: {dicionario[m]}") 
"""

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

"""
frase = "Luciano é muito fera!"

frase_list = []

for n in frase:
    frase_list.append(n)


frase_dict = {}

for n in frase_list:
    frase_dict[n] = 0

a = 0

for n in frase_list:
    for m in frase_dict:
        if n == m:
            a += 1
            frase_dict[n] = frase_dict[n] + a
        else:
            a = 0

print(frase_dict)
"""

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

"""
lista = ["maçã", "banana", "cereja"]

dicionario = {
    "maçã": 0.45, 
    "banana": 0.30, 
    "cereja": 0.65
    }

preco = 0

for n in lista:
    preco += dicionario[n]

print(preco)]
"""
