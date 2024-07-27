# Eliminação de Duplicatas: Objetivo: Dada uma lista de emails, remover todos os duplicados.

"""
emails = ["a@a.com", "a@a.com", "b@a.com"]

emails_unicos = set(emails)

print(emails_unicos)
"""

# 7. Filtragem de Dados: Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

"""
idades = [1, 2, 18, 20]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)
"""

# Ordenação Personalizada:Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

"""
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)
"""

# Agregação de Dados: Objetivo: Dado um conjunto de números, calcular a média.

"""
numeros = [10, 20, 30, 40, 50]

media = sum(numeros)/len(numeros)

print(media)
"""

# Divisão de Dados em Grupos: Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

"""
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valores_pares = [valor for valor in valores if valor % 2 == 0]

valores_impares = [valor for valor in valores if valor % 2 != 0]

print(f"Valores pares {valores_pares}")

print(f"Valores impares {valores_impares}")
"""
