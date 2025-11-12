# Criarum programa onde o usuário digita dois valores e retorna sua soma

while True:
    num_1 = input('Digite o primeiro número: ')
    try:
        num_1_float = float(num_1)
        break
    except:
        print('Valor inválido')

while True:
    num_2 = input('Digite o segundo número: ')
    try:
        num_2_float = float(num_2)
        break
    except:
        print('Valor inválido')


num_1_plus_num_2_float = num_1_float + num_2_float

print(f'A soma de {num_1_float} e {num_2_float} é igual a {num_1_plus_num_2_float}')