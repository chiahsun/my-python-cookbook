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
# ### sort

# %% [markdown]
# #### Sort in Place

# %%
import random
random.seed(9527)
arr = [random.randint(0,10) for _ in range(10)]
print(arr)
arr.sort()
print(arr)

# %% [markdown]
# #### Return Sorted Result

# %%
import random
random.seed(9527)
arr = [random.randint(0,10) for _ in range(10)]
print(sorted(arr))


# %% [markdown]
# #### Sort by Key

# %%
class MyObject:
    def __init__(self, x, y):
        assert y < 10
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()

def my_key(obj):
    return ord(obj.x) * 10 + obj.y
            
arr=[MyObject('b', 1), MyObject('a', 1), MyObject('a', 0), MyObject('c', 3), MyObject('b', 0)]
arr.sort(key=my_key)
arr

# %% [markdown]
# ##### `cmp_to_key`

# %%
from functools import cmp_to_key
# For example, we only want the index sorted by an array
import random
random.seed(9527)
arr = [random.randint(0,10) for _ in range(10)]
print(arr)
indices = list(range(len(arr)))
def my_cmp(i, k):
    if arr[i] == arr[k]:
        return 0
    return -1 if arr[i] < arr[k] else 1
    
indices.sort(key=cmp_to_key(my_cmp))
indices

# %% [markdown]
# #### Reference
#
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/?envType=study-plan&id=programming-skills-i
#
# https://docs.python.org/3/howto/sorting.html#sortinghowto
#
# https://docs.python.org/3/glossary.html#term-key-function
#
# https://docs.python.org/3/library/functools.html#functools.cmp_to_key
#
# https://stackoverflow.com/questions/2531952/how-to-use-a-custom-comparison-function-in-python-3
