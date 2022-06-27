import re
from tkinter import Y
from tracemalloc import start

from soupsieve import match

def myRex(txt):
    pat="fox"
    matches=re.search(pat,txt)
    s=matches.start()
    e=matches.end()
    return (s,e)
print(myRex("The quick brown fox jumps over the lazy dog."))
