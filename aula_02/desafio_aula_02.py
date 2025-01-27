# Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

nome_usuario = input('Digite seu nome: ')


while True:
    try:
        salario_usuario = input('Digite seu salário: ')
        salario_usuario_float = float(salario_usuario)
        break
    except ValueError:
        print('Salário inváido, digite um valor de salário válido')


while True:
    try:
        porncetagem_bonus_usuario = input('Digite a porcentagem do bonus: ')
        porncetagem_bonus_usuario_float = float(porncetagem_bonus_usuario)/100
        break
    except ValueError:
        print(
            'Porcentagem do bonus inválida, digite um valor de porcentagem de bonus válido')


BONUS_FIXO = 1000

bonus = BONUS_FIXO + (salario_usuario_float * porncetagem_bonus_usuario_float)

print(f'O salário do {nome_usuario} é de {
      salario_usuario_float} e seu bonus foi de {bonus}')
