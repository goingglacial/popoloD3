#!/Users/anniekramer/anaconda/bin/python

import csv
import MySQLdb
import sys

def main():
    # open connection to MySQL database
    mydb = MySQLdb.connect(host='localhost', 
        user='anniekramer',
        passwd='anniekramer',
        db='popolo')
    cursor = mydb.cursor()

    csv_data = csv.reader(file('50pops.csv', "rU"))
    
    for row in csv_data:
        city, state, pop = row
        cursor.execute('INSERT INTO 50pops(city, state, pop )' \
          ' VALUES(%r, %r, %r)' % (city, state, pop,))

    # close connection to MySQL database
    cursor.close()
    mydb.commit()
    print "Done! Bravo!"

if __name__ == '__main__':
    main() 