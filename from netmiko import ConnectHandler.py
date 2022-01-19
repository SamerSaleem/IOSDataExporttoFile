# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler
import sys 
with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'samer',
            'password': 'cisco'
        }
 
        net_connect = ConnectHandler(**Router)
 
        hostname = net_connect.send_command('show run | i host')
        showrun = net_connect.send_command('show run')
        showvlan = net_connect.send_command('show vlan')
        showver = net_connect.send_command('show ver | in Version')
        ShowSerial = net_connect.send_command('show ver | in serial')
       
    
    sys.stdout = open('file', 'w')
    print(showvlan + showver + ShowSerial)
    sys.stdout.close()
# Finally close the connection
net_connect.disconnect()