import csv

path_arquivo = 'aula_07/vendas.csv'


def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    '''
    Função que lê um arquivo csv e retorna uma lista de dicionários
    '''
    lista = []
    with open(nome_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    '''
    Função que filtra produtos com o status entrega = True
    '''
    lista_produtos_filtrados = []
    for produto in lista:
        if produto.get('entregue') == 'True':
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados


def somar_valores_produtos_entregues(lista: list[dict]) -> float:
    '''
    Função que soma o valor de produtos com o status entrega = True
    '''
    soma_produtos_filtrados = 0
    for produto in lista:
        soma_produtos_filtrados = + float(produto.get('Venda'))
    return soma_produtos_filtrados


lista_de_produto = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_de_produto)
soma_produtos_entregues = somar_valores_produtos_entregues(produtos_entregues)

print(lista_de_produto)
print(produtos_entregues)
print(soma_produtos_entregues)
