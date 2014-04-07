#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="20.0.0.105", # your host, usually localhost
                     user="root", # your username
                      passwd="ktcloud00", # your password
                      db="world") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
#cur = db.cursor() 

#print cur.execute("SELECT * FROM portal_1")




with db:

    cur = db.cursor()
    cur.execute("SELECT * FROM portal_1")

    for i in range(cur.rowcount):
        
        row = cur.fetchone()
        print row[0], row[1], row[2], row[3]


