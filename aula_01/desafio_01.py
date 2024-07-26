# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

nome = input("Digite seu nome: ")

salario = float(input("Digite seu salário: "))

porcentagem_bonus = float(input("Digite a porcentagem do bonus: "))

CONSTANTE_BONUS = 1000

bonus_final = (CONSTANTE_BONUS + salario) * (porcentagem_bonus/100)

print("O cálculo do bônus é (1000 + salário) * % bonus")

print(f"O seu salário é de R${salario} e seu bonus foi R${bonus_final}")
