#Python program to remove leading zeros from an IP address.

import re
ip=input("Write Ip Address : ")
string = re.sub('\.[0]*', '.', ip)
print(string)
