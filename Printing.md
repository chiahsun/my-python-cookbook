# Printing/Formatting


## f-string

[PEP 498](https://www.python.org/dev/peps/pep-0498/)


```python
print(f"{1 + 1}")
```

    2



```python
for val in [347380.33812199, 525811.212]:
    print(f"Val: {val:>10.3f}")
```

    Val: 347380.338
    Val: 525811.212

