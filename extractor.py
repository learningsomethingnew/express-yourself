import re

def phone_numbers(a_string):
        p = re.compile(r'(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?')
        return re.findall(p, a_string)

def emails(a_string):
    p = re.compile(r'\w*\.\w*@\w*\.\w{3}|\w*@\w*\.\w{3}')
    return re.findall(p, a_string)
