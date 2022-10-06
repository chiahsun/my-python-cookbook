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
# # Built-in Data Structures

# %%
import sys
sys.version

# %% [markdown]
# # Dict

# %%
a = {"one": 1, "two": 2, "three": 3}
print(type(a))
print(a)

# %%
for x in a:
    print(x)

# %%
for x in a.items():
    print(x)
for x, y in a.items():
    print(x, y)

# %%
for x in a.values():
    print(x)

# %%
# https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
inverse_mapping = {number: word for word, number in a.items()}
print(type(inverse_mapping))
print(inverse_mapping)

# %%
inverse_mapping2 = dict((number, word) for word, number in a.items())
print(type(inverse_mapping2))
print(inverse_mapping2)

# %%
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

# https://stackoverflow.com/questions/12992165/
d1 = {'a': 1}
def incrementOrSet2(d, k):
    d[k] += (d[k].get(k, 0) + 1)
incrementOrSet(d1, 'a') 
print(d1)
incrementOrSet(d1, 'b') 
print(d1)    


# %% [markdown]
# # Set

# %%
a = [1, 2, 3, 2, 5]
s = set(a)
print(type(s))
print(s)

# %%
s2 = {x for x in a}
print(type(s2))
print(s2)

# %% [markdown]
# # Iteration

# %% [markdown]
# ## Iterate first k items

# %%
a = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
for index, (word, number) in enumerate(a.items()):
    if index >= 3:
        break
    print(word, number)
