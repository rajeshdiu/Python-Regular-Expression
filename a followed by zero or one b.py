import re

def myRex(pat,txt):
    if re.findall(pat,txt):
        return True
    else:
        return False

pat="^a(b)?"
txt="ab"
print(myRex(pat,txt))