import re

def words(a_string):
    p = re.compile(r'\S\w*\S\w+')
    x = re.findall(p,a_string)
    print(x)
    return x

def phone_number(a_string):
    if len(a_string) > 9:
        a_string = ''.join(e for e in a_string if e.isalnum())
        p = re.compile(r'(?P<area_code>\d{3})(?P<number>\d{7})')
        phone = {}
        #create dict off of response
        for m in p.finditer(a_string):
            phone = m.groupdict()
        #put the dash back in.
        phone['number']= phone['number'][:3]+ '-' +phone['number'][3:]

        return phone
    else:
        return None

def money(a_string):
    p = re.compile(r'^\$?(\d*\.\d{1,2})$')
    return re.findall(p, a_string)


def create_dict(compiler, a_string):
    dic = {}
    for m in compiler.finditer(a_string):
        dic = m.groupdict()
    return dic

l=['$4', '$19']
for mon in l:
    print(money(mon))

################# Words test Strings
# l = ['hello', 'hello world', "raggggg hammer dog", "18-wheeler tarbox", "12"]
#
# for word in l:
#     print(words(word))

# ############Phone Test Strings
# l = ["919-555-1212","(616) 555-1212","9195551212", "919.555.1212", "919 555-1212", "555-1212"]
# #
# for num in l:
#     print(phone_number(num))
