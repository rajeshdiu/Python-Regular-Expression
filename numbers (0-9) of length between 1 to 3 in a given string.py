#  Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

import re
def myRex(txt):
    pat="[0-9]{1,3}"
    if re.findall(pat,txt):
        return True
    else:
        return False


print(myRex('1212rajesh'))
print(myRex('abcdef'))
print(myRex('raejshcpi12'))
print(myRex('123456'))
print(myRex('raj1212diu'))