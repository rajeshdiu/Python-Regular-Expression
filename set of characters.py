import re

from matplotlib.pyplot import text

txt="ABCDEFabrajeshKumar51cdef123450"

pattern="([a-zA-Z0-9]+)"

number=re.findall(pattern,txt)
print(number)

digit_pattern="([0-9]+)"

digit=re.findall(digit_pattern,txt)
print(digit)