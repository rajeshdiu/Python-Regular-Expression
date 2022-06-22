# Python program that matches a word containing 'z'.

import re
def myRex(txt):
    pat="\w+\S*$"
    
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("Razesh Kumar Das"))
print(myRex(" Rajesh Kumaz Das."))
print(myRex("Rajesh Kumar Das "))