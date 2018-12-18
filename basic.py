import matplotlib.pyplot as plt
import csv

x = []
y = []

filename = 'bundesliga_team.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    for row in reader:
        x.append(row[0])
        y.append(row[1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()