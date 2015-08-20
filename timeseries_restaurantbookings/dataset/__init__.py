from os.path import dirname, abspath
import csv

def load():
    rows=[]
    filepath = dirname(abspath(__file__))
    csvin = csv.reader(open(filepath+'/data.csv'), delimiter=',', quotechar='"')
    for row in csvin:
        rows.append([int(x) for x in row])
    return rows
