# https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
print(d)
print(d['a'])
