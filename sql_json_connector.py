import MySQLdb
import json
import collections

db = MySQLdb.connect(host='localhost',
                     user='anniekramer',
                     passwd='anniekramer',
                     db='popolo')
cursor = db.cursor()

cursor.execute("""
    SELECT city, pop
    FROM 50pops
    """)

rows = cursor.fetchall()
result = []
for row in rows:
    d = dict()
    d['city'] = row[0]
    d['pop'] = row[1]
    result.append(d)

j = json.dumps(result)
print j

with open('50pops.json', 'w') as outfile:
    json.dump(j, outfile)

print "Done!"

db.close()