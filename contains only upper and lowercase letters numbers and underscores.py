# Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re
def myRex(txt):
    pat="^[a-zA-Z0-9_]*$"
    
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("Rajesh_kumar_das1212ra"))
print(myRex("Rajesh Kumarz_zas"))
print(myRex("Rajescpi1212_"))