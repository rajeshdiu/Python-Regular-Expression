# Python program that matches a word at the end of a string, with optional punctuation.

import re
def myRex(txt):
    pat="\w+\S*$"
    
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("Rajesh Kumar Das"))
print(myRex(" Rajesh Kumar Das."))
print(myRex("Rajesh Kumar Das "))