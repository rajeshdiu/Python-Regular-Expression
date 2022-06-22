# Python program that matches a word containing 'z', not at the start or end of the word.

import re
def myRex(txt):
    pat="\Bz\B"
    
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("Razesh Kumarz Das"))
print(myRex("Razesh Kumaz Daz."))
print(myRex("Rajesh Kumarz zas"))