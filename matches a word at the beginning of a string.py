# Python program that matches a word at the beginning of a string.

import re
def myRex(txt):
    pat="^\w+"
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("Rajesh Kumar Das"))
print(myRex(" Rajesh Kumar Das"))
print(myRex("Rajesh Kumar Das "))