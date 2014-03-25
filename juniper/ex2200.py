from jnpr.junos import Device
from jnpr.junos.utils.config import Config
dev = Device(host='20.0.2.31',user='admin',password='ktcloud00')
dev.open()


cu = Config(dev)
set_cmd = 'set system login message "0324"'
print cu.load(set_cmd, format='set')
print cu.pdiff()

#print cu.commit_check()

dev.close()



