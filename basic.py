import csv

filename = 'bundesliga_team.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    vals = []
    for row in reader:
        vals.append(row[2])
        print(vals)