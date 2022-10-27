# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Dictionary
# ## Constructor

# %%
import sys
sys.version

# %%
d = {"one": 1, "two": 2, "three": 3}
print(type(d))
print(d)

# %% [markdown]
# ### Dictionary comprehesion

# %%
a = ["one", "two", "three"]
d = { c: i for i, c in enumerate(a) }
d

# %% [markdown]
# #### Reverse a mapping

# %%
# https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
inverse_mapping = {number: word for word, number in d.items()}
print(type(inverse_mapping))
print(inverse_mapping)

# %%
inverse_mapping2 = dict((number, word) for word, number in d.items())
print(type(inverse_mapping2))
print(inverse_mapping2)

# %% [markdown]
# ## Iteration

# %%
for x in d:
    print(x)

# %%
for x in d.items():
    print(x)
for x, y in d.items():
    print(x, y)

# %%
for x in d.values():
    print(x)

# %% [markdown]
# ## Increment Value in a Dictionary

# %%
# https://stackoverflow.com/questions/12992165/python-dictionary-increment
d1 = {'a': 1}

def incrementOrSet(d, k):
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
incrementOrSet(d1, 'a') 
print(d1)
incrementOrSet(d1, 'b') 
print(d1)

# %%
# https://stackoverflow.com/questions/12992165/
d2 = {'a': 1}
def incrementOrSet2(d, k):
    d[k] = (d.get(k, 0) + 1)
incrementOrSet2(d2, 'a') 
print(d2)
incrementOrSet2(d2, 'b') 
print(d2)    

# %%
d3 = {'a': 1}
def incrementOrSet3(d, k):
    d.setdefault(k, 0)
    d[k] += 1
incrementOrSet3(d3, 'a') 
print(d3)
incrementOrSet3(d3, 'b') 
print(d3)  

# %%
# https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict
d4 = defaultdict(int)
d4['a'] += 1
print(d4)
print(d4['a'])
