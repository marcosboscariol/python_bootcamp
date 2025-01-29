# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.

'''
quantidade = [1, -1]
preco = [1, 2]
q = 0
p = 0

for dados in quantidade:
    if dados < 0:
        q += 1


for dados in preco:
    if dados < 0:
        p += 1


if q or p > 1:
    print('Dados Inválidos')
else:
    print('Dados Válidos')
'''


# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

'''
log = {'timestamp': '2021-06-23 10:00:00',
       'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log)
'''

# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

'''
i = 0
e = 0

usuarios = [
    {
        'id_usuario': 1,
        'informacoes': {
            'email': 'aaa@aaa',
            'idade': 19
        }
    },
    {
        'id_usuario': 2,
        'informacoes': {
            'email': 'bb@bbbb',
            'idade': 30
        }
    }
]

for usuario in usuarios:
    if '@' not in (usuario['informacoes']['email']):
        e = + 1


for usuario in usuarios:
    if (usuario['informacoes']['idade']) < 18 or (usuario['informacoes']['idade']) > 65:
        i = + 1

erros = []

if e > 0:
    erros.append('Erro de e-mail')

if i > 0:
    erros.append('Erro de idade')

if len(erros) > 0:
    print('Erros encontrados: ')
    for erro in erros:
        print(erro)
else:
    print('Dados Válidos')
'''

# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

'''
transacao_suspeita = []

transacao = {'valor': 12000, 'hora': 19}

for chave in transacao:
    if chave == 'valor':
        if transacao[chave] > 10000:
            transacao_suspeita.append(
                'Valor maior que R$ 10.000,00')
    elif chave == 'hora':
        if transacao[chave] < 9 or transacao[chave] > 18:
            transacao_suspeita.append(
                'Realizada fora do horário comercial')

if transacao_suspeita:
    print('Transação suspeita pelos motivos: ')
    for i in transacao_suspeita:
        print(i)
else:
    print('Transação Normal')
'''

# Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

'''
palavra = 'banana'

palavra_list = list(palavra)

contagem = {}

for letra in palavra_list:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)
'''

# Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

'''
numeros = [1, 2, 5, 10]

numeros_normalizados = []

for numero in numeros:
    numeros_normalizados.append(numero/max(numeros))

print(numeros_normalizados)
'''

# Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

'''
usuarios = [
    {
        'id_usuario': 1,
        'nome': 'Marcos',
        'email': 'aaa@aaa'
    },
    {
        'id_usuario': 2,
        'nome': '',
        'email': 'aaa@aaa'
    }
]

for usuario in usuarios:
    for chave in usuario:
        if (usuario[chave]) == '':
            print(usuario, chave)
'''

# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

'''
numeros = [1, 2, 3, 4, 5]

numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(numeros_pares)
'''

# Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

'''
vendas = [
    {
        'categoria': 1,
        'valor': 10
    },
    {
        'categoria': 1,
        'valor': 20
    }
]

vendas_categoria = 0

for venda in vendas:
    if venda['categoria'] == 1:
        vendas_categoria = vendas_categoria + venda['valor']

print(vendas_categoria)
'''

# Exercícios com WHILE

# Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

'''
while True:
    input_usuario = input('Digite algo ou aperte "S" para sair: ')
    if input_usuario == 'S':
        break
'''


# Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

'''
while True:
    numero_usuario = input('Digite um número inteiro entre 1 e 10: ')
    try:
        numero_usuario_int = int(numero_usuario)

        if int(numero_usuario) <= 10 and int(numero_usuario) >= 0:
            break
        else:
            print('Valor inválido')
    except ValueError:
        print('Valor inválido')
'''

# Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

'''
maximo_tentativas = 5

tentativas = 0

conexao_disponivel = False

while conexao_disponivel == False and tentativas < maximo_tentativas:
    tentativas += 1
    print(f'Falha de conexão, tentativa {
          tentativas}, com um limite de {maximo_tentativas}')
'''

# Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.


lista = [1, 2, 3, 4, 5]

item_a_ser_encontrado = 5

'''
for numero in lista:
    if numero == item_a_ser_encontrado:
        print(numero)
        break
'''
