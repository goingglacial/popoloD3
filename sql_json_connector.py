import MySQLdb
import json
import collections

connstr = 'DRIVER={SQL Server};SERVER=ServerName;DATABASE=popolo;'
conn = MySQLdb.connect(connstr)
cursor = conn.cursor()

cursor.execute("""
    SELECT *
    FROM 50pops
    """)

rows = cursor.fetchall()

# Convert MySQL query to objects of key-value pairs
# json file = list of objects --> [{},{},{}]

objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['city'] = row.city
    d['pop'] = row.pop

j = json.dumps(objects_list)
objects_file = '50pops.json'
f = open(objects_file, 'w')

print "Done!"

conn.close()