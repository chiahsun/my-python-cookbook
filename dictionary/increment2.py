# https://stackoverflow.com/questions/12992165/

d = {'a': 1}
def incrementOrSet2(d, k):
    d[k] = (d.get(k, 0) + 1)

incrementOrSet2(d, 'a')
print(d)
incrementOrSet2(d, 'b')
print(d)
