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
# # Set
# ## Constructor

# %%
a = [1, 2, 3, 2, 5]
s = set(a)
print(type(s))
s

# %% [markdown]
# ### Set Comprehension

# %%
a = ["one", "two", "three"]
s = { x for x in a }
print(type(s))
s

# %%
d = {"one": 1, "two": 2, "three": 3}
s = { (a, b) for a, b in d.items() }
print(type(s))
s
