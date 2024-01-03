d = {"one": 1, "two": 2, "three": 3}

inverse_mapping = {number: word for word, number in d.items()}
print(type(inverse_mapping))
print(inverse_mapping)

# %%
inverse_mapping2 = dict((number, word) for word, number in d.items())
print(type(inverse_mapping2))
print(inverse_mapping2)

