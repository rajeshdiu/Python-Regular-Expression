# Python program to check for a number at the end of a string.
import re
def myRex(txt):
    pat="\.*[0-9]$"
    if re.findall(pat,txt):
        return True
    else:
        return False


print(myRex('abcdef'))
print(myRex('abcdef6'))