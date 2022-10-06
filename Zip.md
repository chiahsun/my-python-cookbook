#### zip


```python
a = [1, 2, 3]
b = ["One", "Two", "Three"]
print(list(zip(a, b)))
```

    [(1, 'One'), (2, 'Two'), (3, 'Three')]



```python
print(*zip(a, b))
```

    (1, 'One') (2, 'Two') (3, 'Three')



```python
c, d = zip(*zip(a, b))
print(c)
print(d)
print(list(zip(*zip(a, b))))
```

    (1, 2, 3)
    ('One', 'Two', 'Three')
    [(1, 2, 3), ('One', 'Two', 'Three')]

