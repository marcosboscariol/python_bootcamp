# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

"""
num_1 = int(input("Digite o primeiro numero: "))

num_2 = int(input("Digite o segundo numero: "))

resultado = num_1 + num_2

print(f"A soma de {num_1} e {num_2} é {resultado}")
"""

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

"""
num = int(input("Digite um número: "))

resultado = num % 5

print(f"O resto da disvisão de {num} por 5 é {resultado}")
"""

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

"""
num_1 = int(input("Digite o primeiro numero: "))

num_2 = int(input("Digite o segundo numero: "))

resultado = num_1 * num_2

print(f"A multiplicação de {num_1} e {num_2} é {resultado}")
"""

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

"""
num_1 = int(input("Digite o primeiro numero: "))

num_2 = int(input("Digite o segundo numero: "))

resultado = num_1 // num_2

print(f"A divisão inteira de {num_1} e {num_2} é {resultado}")
"""

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

"""
num = int(input("Digite um número: "))

resultado = num ** 2

print(f"O quedrado de {num} é {resultado}")
"""

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

"""
num_1 = float(input("Digite o primeiro numero: "))

num_2 = float(input("Digite o segundo numero: "))

resultado = num_1 + num_2

print(f"A soma de {num_1} e {num_2} é {resultado}")
"""

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

"""
from statistics import mean
num_1 = float(input("Digite o primeiro numero: "))

num_2 = float(input("Digite o segundo numero: "))

list_mean = [num_1, num_2]

resultado = mean(list_mean)

print(f"A média de {num_1} e {num_2} é {resultado}")
"""

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

"""
base = float(input("Digite a base: "))

expoente = float(input("Digite o expoente: "))

resultado = base ** expoente

print(f"{base} eelevado a {expoente} é {resultado}")
"""

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

"""
temperatura_celsius = float(input("Digite a temperatura em Celcius: "))

temperatura_fahrenhiet = temperatura_celsius * 1.8 + 32

print(f'{temperatura_celsius} celsius é igual a {temperatura_fahrenhiet} F')
"""

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

"""
from math import pi
raio = float(input("Digite o raio: "))

area = pi * raio ** 2

print(f"Com um raio {raio} o circulo tem {area} de área")
"""

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

"""
frase_usuario = input("Digite uma frase: ")

frase_upper = frase_usuario.upper()

print(f"A sua frase em maiúsculo fica: {frase_upper}")
"""

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

"""
nome_usuario = input("Digite seu nome: ")

nome_lower = nome_usuario.lower()

print(f"Seu nome em minúsculo fica: {nome_lower}")
"""

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

"""
frase = input("Por favor, insira uma frase: ")

frase_sem_espacos = frase.strip()

print(f"Frase sem espaços em branco no início e no final: {frase_sem_espacos}")
"""

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

"""
data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")

data_split = data_usuario.split("/")

print(
    f"A data {data_usuario} separada fica: Dia: {data_split[0]}, Mês: {data_split[1]}, Ano: {data_split[2]}")
"""

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

"""
string_1 = input("Digite a primeira String: ")

string_2 = input("Digite a segunda String: ")

string_final = (string_1 + string_2)

print(f"A String final fica: {string_final}")
"""

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

"""
opcao_1 = bool(input("Para True, digite algo, para False, não digite nada: "))

opcao_2 = bool(input("Para True, digite algo, para False, não digite nada: "))

resultado = opcao_1 and opcao_2

print(f"O resultado de {opcao_1} e {opcao_2} é {resultado}")
"""

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

"""
opcao_1 = bool(input("Para True, digite algo, para False, não digite nada: "))

opcao_2 = bool(input("Para True, digite algo, para False, não digite nada: "))

resultado = opcao_1 or opcao_2

print(f"O resultado de {opcao_1} e {opcao_2} é {resultado}")
"""

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

"""
opcao_1 = bool(input("Para True, digite algo, para False, não digite nada: "))

resultado = not opcao_1

print(f"O contrario de {opcao_1} é {resultado}")
"""

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

"""
numero_1 = float(input("Digite o primeiro número: "))

numero_2 = float(input("Digite o segundo número: "))

if numero_1 == numero_2:
    print(f"O número {numero_1} é igual ao número {numero_2}")
else:
    print(f"O número {numero_1} não é igual ao número {numero_2}")
"""

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

"""
numero_1 = float(input("Digite o primeiro número: "))

numero_2 = float(input("Digite o segundo número: "))

if numero_1 != numero_2:
    print(f"O número {numero_1} é diferente do número {numero_2}")
else:
    print(f"O número {numero_1} não é diferente ao número {numero_2}")
"""

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
