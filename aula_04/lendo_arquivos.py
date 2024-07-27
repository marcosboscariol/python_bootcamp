import csv

# Não estou passando o caminho pois o arquivo está na mesmo pasta
path = "c:\\Users\\marco\\OneDrive\\Documentos\\jornada_de_dados\\python_bootcamp\\aula_04\\exemplo.csv"

arquivo_csv = []

with open(path, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for n in leitor_csv:
        arquivo_csv.append(n)

print(arquivo_csv)
