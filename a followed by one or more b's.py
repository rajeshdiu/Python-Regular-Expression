import re


def myRex(pat,txt):
    if re.findall(pat,txt):
        return True
    else:
        return False

txt=input("Enter String : ")
pat="^a(b+)$"