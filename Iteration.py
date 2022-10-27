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
# # Iteration
# ## Iteration First k Items

# %%
K = 3
a = [1, 2, 3, 4, 5]
for i in range(min(len(a), K)):
    print(a[i])

# %%
d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
for index, (word, number) in enumerate(d.items()):
    if index >= 3:
        break
    print(word, number)

# %%
b = [1, 2, 3, 4, 5]
for index, x in enumerate(b):
    if index >= 3:
        break
    print(x)

# %%
# You can also use conditional for loop but it's less efficient since we can break in the middle of the iteration

# %% [markdown]
# ## Conditional For-Loop
# ### Iteration only even number index

# %%
b = [0, 1, 2, 3, 4]
for index, x in enumerate(b):
    if index % 2 == 1:
        continue
    print(index, x)

# %%
# https://stackoverflow.com/questions/12986996/conditional-for-in-python
for index, x in ((index, x) for index, x in enumerate(b) if index % 2 == 0):
    print(index, x)

# %%
for index, x in filter(lambda tpl: tpl[0] % 2 == 0, enumerate(b)):
    print(index, x)
