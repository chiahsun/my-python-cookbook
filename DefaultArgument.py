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

# %%
def add_one(d={}):
    if 1 in d:
        d[1] += 1
    else:
        d[1] = 1
    return d
add_one()

# %%
add_one()

# %%
add_one()
