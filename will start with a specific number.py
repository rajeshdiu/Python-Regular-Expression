#  Python program where a string will start with a specific number.
import re
def myRex(txt):
    pat="^\d"
    
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("Rajescpi1212_"))
print(myRex("5raesh"))
print(myRex("05454raesh"))