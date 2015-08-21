import csv
import psycopg2
from pytz import timezone, utc
from datetime import date, timedelta

def convert_datetime_across_timezones(d, t1, t2):
    """
    converts a datetime from one timezone to another.
    It answers the question:
    what time was in this timezone when it was that time in that timezone?
    e.g. convert_datetime_across_timezones(
             datetime.now(), timezone('Europe/Berlin'), utc)

    """
    d_dt = t1.localize(d, is_dst=True)
    return d_dt.astimezone(t2).replace(tzinfo=None)

conn = psycopg2.connect("dbname='resmio' user='postgres' host='localhost' password='abcdEF123456'")
timezones = {}

#filter enabled
cur = conn.cursor()
cur.execute("select id,timezone from bookoya_facility where enabled;")#2070
for row in cur.fetchall():
    timezones[row[0]] = row[1]
    #csvout.writerow(row)

mindate = None
maxdate = date(2015,8,18)
counts={}

import dateutil.parser
cur.execute("select facility_id,date from bookoya_booking;")
for row in cur.fetchall():
    facility_id = row[0]
    utcdatetime = row[1].replace(tzinfo=None)
    if facility_id in timezones:
        tz = timezones[facility_id]
        localdate = convert_datetime_across_timezones(utcdatetime, utc, timezone(tz)).date()
        if facility_id not in counts:
            counts[facility_id] = {}
        if localdate not in counts[facility_id]:
            counts[facility_id][localdate] = 0
        counts[facility_id][localdate] += 1
        if localdate.year<2011:
            continue
        if not mindate or localdate < mindate:
            mindate = localdate

print mindate
#import sys
#sys.path.insert(1,'/usr/share/pyshared')
plot = False
if plot:
    import matplotlib
    import matplotlib.pyplot as plt
    #matplotlib.use("Agg")

#print mindate,maxdate
facility_id = list(counts.keys())[0]
csvout = csv.writer(open('data.csv', 'w'), delimiter=',', quotechar='"')
for facility_id in counts:
    #print facility_id
    dt = mindate
    row=[]
    while dt<maxdate:
        count = 0
        if dt in counts[facility_id]:
            count = counts[facility_id][dt]
        row.append(count)
        #print facility_id,dt,count
        dt = dt+timedelta(days=1)
    if sum(row)>100:
        print row
        csvout.writerow(row)
        if plot:
            plt.plot(range(0,len(row)),row)

if plot:
    size = plt.gcf().get_size_inches()
    plt.gcf().set_size_inches((size[0]*4,size[1]))
    plt.savefig('plot.pdf')



exit(0)
cur = conn.cursor()
cur.execute("select facility_id,email from bookoya_booking;")
#select date(date),facility_id,count(*) as count from bookoya_booking group by date(date),facility_id;
for row in cur.fetchall():
    csvout.writerow(row)
