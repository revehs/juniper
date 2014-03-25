from jnpr.junos import Device
from jnpr.junos.utils.config import Config
dev = Device(host='20.0.2.31',user='admin',password='ktcloud00')
dev.open()


cu = Config(dev)
#set_cmd = {"set system login message 'hi_0325'":
#           "set interfaces vlan unit 3150 family inet address 20.0.0.1/24"}


print cu.load(path="/home/hans/git/juniper/juniper/config.set", format='set')
print cu.pdiff()

#print cu.commit_check()

dev.close()



