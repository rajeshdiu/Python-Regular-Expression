#  Python program to find the sequences of one upper case letter followed by lower case letters.

import re
def myRex(txt):
    pat="^[A-Z]+[a-z]+$"
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("ab"))
print(myRex("rajesh_das"))