import csv

def ler_csv(arquivo_csv: str) -> list[dict]:
    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor= csv.DictReader(arquivo)
        return list(leitor)
    

def produtos_entregues(lista_produtos: list[dict]) -> list[dict]:
    lista_produtos_entregues = []
    for produto in lista_produtos:
        if produto.get('entregue') == 'True':
            lista_produtos_entregues.append(produto)
    return lista_produtos_entregues

def soma_valor_produtos_entregues(lista_produtos_entregues: list[dict]) -> float:
    valor_total = 0.0
    for produto in lista_produtos_entregues:
        valor_total += float(produto.get('price'))

    return valor_total