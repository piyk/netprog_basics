#! /usr/bin/env python


import csv
from pprint import pprint


readcsv = open("csv_example.csv").read()

#pprint(readcsv)

csvfile = open("csv_example.csv")
csv_py  = csv.reader(csvfile)

for row in csv_py:
	print("{} is in {} and IP {}".format(row[0],row[1],row[2]))



