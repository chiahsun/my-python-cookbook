# Miscellaneous

## Iterate two vectors by tuples `zip()`


```python
x = [1, 2, 3]
y = [4, 5, 6]
for a in zip(x, y):
    print(f"x = {a[0]} y = {a[1]}")
```

    x = 1 y = 4
    x = 2 y = 5
    x = 3 y = 6



```python
def euclidean_distance(p1, p2):
    return sum([(a[0] - a[1]) ** 2 for a in zip(p1, p2)]) ** 0.5

print(euclidean_distance([1], [3]))
print(euclidean_distance([2, 6], [5, 2]))
```

    2.0
    5.0


## Find argmin or argmax `min(, key = )`


```python
min([1, 2, 3, 4, 5], key = lambda x: x**2 - 4*x)
```




    2




```python
max([1, 2, 3, 4, 5], key = lambda x: -x**2 + 4*x)
```




    2



### Reference

[wiki arguments of the maxima/minimum](https://en.wikipedia.org/wiki/Arg_max)
