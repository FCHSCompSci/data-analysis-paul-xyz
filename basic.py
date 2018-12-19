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
        y.append(row[11])
        x.append(row[1])

plt.ylabel('Red Card #')
plt.xlabel('Team Name')
plt.bar(x,y)
plt.show()