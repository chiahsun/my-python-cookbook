
d = {'a': 1}
def incrementOrSet3(d, k):
    d.setdefault(k, 0)
    d[k] += 1

incrementOrSet3(d, 'a')
print(d)
incrementOrSet3(d, 'b')
print(d)
