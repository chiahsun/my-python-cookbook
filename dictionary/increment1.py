# https://stackoverflow.com/questions/12992165/python-dictionary-increment
d = {'a': 1}

def incrementOrSet(d, k):
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
incrementOrSet(d, 'a')
print(d)
incrementOrSet(d, 'b')
print(d)
