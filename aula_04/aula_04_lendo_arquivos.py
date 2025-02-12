import csv

file_path: str = 'aula_04/exemplo.csv'

csv_file: list = []

with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for line in csv_reader:
        csv_file.append(line)

print(csv_file)
