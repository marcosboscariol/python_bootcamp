import funcoes

vendas_itens = funcoes.ler_csv('vendas.csv')

produtos_entregues = funcoes.produtos_entregues(vendas_itens)

valor_total_produtos_entregues = funcoes.soma_valor_produtos_entregues(produtos_entregues)

print(valor_total_produtos_entregues)

