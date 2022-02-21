import csv

with open('list.csv', 'r', encoding='utf8') as csv_file:

    csv_reader = csv.reader(csv_file)
    print(list(csv_reader))
    # print(type(csv_reader))
    for row in csv_reader:
        print()
