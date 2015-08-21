from os.path import dirname, abspath
from datetime import date, timedelta
import csv

def load():
    rows=[]
    filepath = dirname(abspath(__file__))
    csvin = csv.reader(open(filepath+'/data.csv'), delimiter=',', quotechar='"')
    for row in csvin:
        rows.append([int(x) for x in row])
    return rows

def get_dates_array():
    mindate = date(2011,11,14)
    maxdate = date(2015,8,18)
    row=[]
    dt = mindate
    while dt<maxdate:
        row.append(dt)
        dt = dt+timedelta(days=1)
    return row
