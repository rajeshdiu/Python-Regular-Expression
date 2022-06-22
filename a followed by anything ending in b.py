# Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re
def myRex(txt):
    pat="a.*?b$"
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("ab"))
print(myRex("aabAbbbc"))
print(myRex("accb"))