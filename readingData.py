import csv

with open('matches.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#   	print(row)
#       print(row[0])
#       print(row[0],row[1],row[2],)

    your_list = list(readCSV)
print(your_list[1])
