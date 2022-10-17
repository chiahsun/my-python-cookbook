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
# # List
# ## Add Element to List

# %%
a = [0, 1, 2]
a.append(3)
a

# %%
a.extend([4, 5])
a

# %% [markdown]
# ## Get Position of the Element

# %%
a.index(5)

# %% [markdown]
# ## List Comprehension

# %%
print([a ** 2 for a in range(10) if a % 3 == 0])

# %% [markdown]
# ## Arg Max or Arg Min

# %%
b = [23, 7, 44, 2]
print(b.index(max(b)))

# %%
print(b.index(min(b)))
