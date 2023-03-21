import csv

with open("Archives\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    
    for row in reader:
        print(row)