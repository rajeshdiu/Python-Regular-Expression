import re

def myRex(txt):
    pat="^ab{2,3}"
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("ab"))
print(myRex("abb"))
print(myRex("abbb"))
print(myRex("ac"))