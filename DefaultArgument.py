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
# #### The Mutable Default Argument Problem
#
# [SO](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument)
#
# [SO](https://stackoverflow.com/questions/10676729/why-does-using-arg-none-fix-pythons-mutable-default-argument-issue)
#

# %%
def add_element(e, l=[]):
    l.append(e)
    return l
a = []
add_element(1, a)

# %%
add_element(2, a)

# %%
a

# %%
b = []
add_element(1, b)

# %%
add_element(1)

# %%
add_element(2)


# %% [markdown]
# ##### Solution

# %%
def add_element(e, l=None):
    if l is None:
        l = []
    l.append(e)
    return l
a = []
add_element(1, a)

# %%
add_element(2, a)

# %%
a

# %%
add_element(1)

# %%
add_element(2)
