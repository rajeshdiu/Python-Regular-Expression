# Python program to find sequences of lowercase letters joined with a underscore.
import re
def myRex(txt):
    pat="^[a-z]+_[a-z]+$"
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("ab"))
print(myRex("abbb"))
print(myRex("a_c"))
print(myRex("rajesh_das"))