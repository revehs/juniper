#! /usr/bin/env python

import sys
print sys.path

from jnpr.junos import Device
from netaddr import *
from jnpr.junos.utils.config import Config
import MySQLdb
   
print "10111"
#val = raw_input("Customer ID:")
#print val
# val = "ucloudadd1@yopmail.com"
f = file("emailconfig.set","r")
val = f.read()
print val

db= MySQLdb.connect(host="20.0.0.103",user="root",passwd="ktcloud00",db="test")
cursor=db.cursor()

query_cmd="select * from cip_portal where customer_id = '"+val+"';"
cursor.execute(query_cmd)
result =  cursor.fetchall()
"""print result"""

print "11111"
  
dev = Device(host='20.0.2.31',user='admin',password='password')
dev.open()
 
def get_net(gateway, netmask):
    ip = IPAddress(netmask)
    netbit = ip.netmask_bits()
    tempformat= gateway+'/'+str(netbit)
    netname = IPNetwork(tempformat).network
    realnet = str(netname) +'/'+ str(netbit)
    return realnet 
 
vlan = result[0][4]
vlan_name = 'vlan_'+ result[0][4]
filter_name = result[0][4]+'_ACL'
vlan_description = result[0][0]
src_net = get_net(result[0][2], result[0][3])
src_gw=result[0][2]
dst_net=  get_net(result[0][6],result[0][7])
  
cu = Config(dev)
set_cmd = 'set vlans '+vlan_name+' l3-interface vlan.'+vlan+""" 
"""'set interfaces vlan unit '+ vlan + ' description ' +vlan_description+"""
"""'set interfaces vlan unit '+ vlan + ' family inet address '+src_gw+"""
"""'set firewall family inet filter '+filter_name+' term 10 from source-address '+src_net+"""
"""'set firewall family inet filter '+filter_name+' term 10 from destination-address '+dst_net+"""
"""'set firewall family inet filter '+filter_name+' term 10 then accept'"""
"""'set firewall family inet filter '+filter_name+' term 20 from source-address '+dst_net+"""
"""'set firewall family inet filter '+filter_name+' term 20 then discard'"""
"""'set firewall family inet filter '+filter_name+' term default then accept'"""
"""'set interfaces vlan unit 3455 family inet filter input '+filter_name 

print(type(set_cmd))
print(set_cmd)
print "1211"

print cu.load(set_cmd, format='set')
print cu.pdiff()
#print cu.commit()
dev.close()
