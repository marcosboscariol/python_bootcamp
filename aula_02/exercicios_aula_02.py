# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

'''
numero_usuario_1 = input('Digite o primeiro número: ')
numero_usuario_2 = input('Digite o segundo número: ')
numero_usuario_1_int = int(numero_usuario_1)
numero_usuario_2_int = int(numero_usuario_2)

soma = numero_usuario_1_int + numero_usuario_2_int
print(f'A soma dos números {numero_usuario_1_int} e {
      numero_usuario_2_int} é {soma}')
'''

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

'''
numero_usuario = input('Digite um número: ')
numero_usuario_float = float(numero_usuario)

resto = numero_usuario_float % 5

print(f'O resto da divisão de {numero_usuario_float} por 5 é {resto}')
'''

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

'''
while True:
    numero_usuario_1 = input('Digite o primeiro número: ')
    try:
        numero_usuario_1_float = float(numero_usuario_1)
        break
    except ValueError as e:
        print(f'Erro {e}, digite um número váido: ')
while True:
    numero_usuario_2 = input('Digite o segundo número: ')
    try:
        numero_usuario_2_float = float(numero_usuario_2)
        break
    except ValueError as e:
        print(f'Erro {e}, digite um número váido: ')

resultado = numero_usuario_1_float * numero_usuario_2_float

print(f'O resultado de {numero_usuario_1_float} x {
      numero_usuario_2_float} é {resultado}')
'''


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.


while True:
    numero_1_usuario = input('Digite o primeiro número: ')
    try:
        numero_1_usuaio_int = int(numero_1_usuario)
        break
    except ValueError as e:
        print('Número inválido, digite um número inteiro: ')
while True:
    numero_2_usuario = input('Digite o segundo número: ')
    try:
        numero_2_usuaio_int = int(numero_2_usuario)
        break
    except ValueError as e:
        print('Número inválido, digite um número inteiro: ')

resultado = numero_1_usuaio_int // numero_2_usuaio_int

print(f'A divisão de a divisão inteira de {
      numero_1_usuaio_int} e {numero_2_usuaio_int} é {resultado}')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
