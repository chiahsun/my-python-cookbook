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
# # Printing/Formatting
#
#
# ## f-string
#
# [PEP 498](https://www.python.org/dev/peps/pep-0498/)

# %%
print(f"{1 + 1}")

# %%
for val in [347380.33812199, 525811.212]:
    print(f"Val: {val:>10.3f}")

# %%
for val in range(11):
    print(f"{val:02}")

# %%
