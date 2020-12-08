import csv

path="C:\Users\corei5\OneDrive\Escritorio\Capacitación\U. Michigan\Python\Gift_Cards.tsv"
f = open(path)
reader = csv.reader(f,delimiter='\t')
next(reader)
