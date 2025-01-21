# Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input('Digite seu nome: ')

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = input('Digite seu salário: ')
salario_usuario_float = float(salario_usuario)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = input('Digite a porcentagem do bônus recebido: ')
bonus_usuario_float = float(bonus_usuario)

# 4) Calcule o valor do bônus final
bonus_final = 1000 + (bonus_usuario_float/100) * salario_usuario_float

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'O nome do usuário é {nome_usuario}')
print(f'O salário do usuário é R$ {salario_usuario_float:.2f}')
print(f'A porcentagem do bônus do usuário é {bonus_usuario_float:.2f} %')
print(f'O bônus final do usuário é de R$ {bonus_final}')
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
