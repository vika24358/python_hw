import csv

with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        if row[5] == "UA":
            print(row[2])
