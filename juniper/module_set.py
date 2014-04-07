#! /usr/bin/env python

from jnpr.junos.device import Device
from jnpr.junos.utils.config import Config
import MySQLdb

dev = Device(host='20.0.2.31',user='admin',password='ktcloud00')
dev.open()

cu = Config(dev)

print cu.load(path="/home/hans/git/juniper/juniper/config.set", format='set')
print cu.pdiff()

dev.close()



