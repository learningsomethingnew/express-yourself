
import re

def binary(a_string):
    print(a_string)
    a_string = str(a_string)
    p = re.compile(r'\b[01]+\b')
    return re.match(p, a_string)

print(binary(10))
