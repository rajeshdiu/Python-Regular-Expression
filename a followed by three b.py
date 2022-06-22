import re
def myRex(txt):
    
    pat="^ab{3}?"
    if re.findall(pat,txt):
        return True
    else:
        return False

print(myRex("abbb0"))
print(myRex("abbb"))
print(myRex("ab"))
print(myRex("abcabbb"))
print(myRex("ac"))