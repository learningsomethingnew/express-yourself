
import re

def binary(a_string):
    print(a_string)
    a_string = str(a_string)
    p = re.compile(r'\b[01]+\b')
    return re.match(p, a_string)

def binary_even(a_string):
    if binary:
        temp_int = int(a_string)
        if temp_int % 2 == 0:
            return True
        else:
            return False

def hex(a_string):
    p = re.compile(r'\b[0-9A-F]+\b')
    print(a_string)
    return re.match(p, a_string)

print(hex("CAFE"))
