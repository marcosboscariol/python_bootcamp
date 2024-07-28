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

# Atualização de Dados: Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

"""
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

for i in produtos:
    if i["id"] == 1:
        i["preço"] = 90

print(produtos)
"""

# Fusão de Dicionários: Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

"""
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario3 = {**dicionario1, **dicionario2}

print(dicionario3)

dicionario4 = dicionario1

dicionario4.update(dicionario2)

print(dicionario4)
"""

# Filtragem de Dados em Dicionário: Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

"""
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {
    produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)
"""

# Extração de Chaves e Valores: Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

"""
dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)
print(dicionario.keys())
"""

# Contagem de Frequência de Itens: Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)
