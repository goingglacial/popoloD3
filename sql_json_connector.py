import MySQLdb
import json
import collections

db = MySQLdb.connect(host='localhost',
                     user='anniekramer',
                     passwd='anniekramer',
                     db='popolo')
cursor = db.cursor()

cursor.execute("""
    SELECT city, state, pop
    FROM 50pops
    """)

rows = cursor.fetchall()
result = []
for row in rows:
    d = dict()
    d['city'] = row[0]
    d['state'] = row[1]
    d['pop'] = row[2]
    result.append(d)

print(json.dumps((result), sort_keys=True, indent=4))
content = (json.dumps((result), sort_keys=True, indent=4))

with open('popolo.json', 'w') as outfile:
    json.dump(content, outfile)

print "Done!"

db.close()