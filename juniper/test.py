#!/usr/bin/python
# import MySQLdb
# 
# db = MySQLdb.connect(host="20.0.0.105", # your host, usually localhost
#                      user="root", # your username
#                       passwd="ktcloud00", # your password
#                       db="world") # name of the data base

from netaddr import *
#import pprint

def get_net(gateway, netmask):
    ip = IPAddress(netmask)
    netbit = ip.netmask_bits()
    tempformat= gateway+'/'+str(netbit)
    netname = IPNetwork(tempformat).network
    realnet = str(netname) +'/'+ str(netbit)
    return realnet 

print get_net('10.17.5.188', '255.255.255.224')

# you must create a Cursor object. It will let
#  you execute all the queries you need
#cur = db.cursor() 

#print cur.execute("SELECT * FROM portal_1")
#hshs11



# with db:
# 
#     cur = db.cursor()
#     cur.execute("SELECT * FROM portal_1")
# 
#     for i in range(cur.rowcount):
#         
#         row = cur.fetchone()
#         print row[0], row[1], row[2], row[3]


