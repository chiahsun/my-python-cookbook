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
# ### zip

# %%
a = [1, 2, 3]
b = ["One", "Two", "Three"]
print(list(zip(a, b)))

# %%
print(*zip(a, b))

# %%
c, d = zip(*zip(a, b))
print(c)
print(d)
print(list(zip(*zip(a, b))))
