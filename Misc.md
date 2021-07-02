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




```python
import pandas as pd
# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
data = {'a': [1, 2], 'b': [2, -7], 'c': [4, 2], 'd': [9, -1]}
X = pd.DataFrame(data = data)
X
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>-7</td>
      <td>2</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# X.loc[1, :]
min(list(X.columns), key = lambda col: X.loc[1, col])
```




    'b'



### Reference

[wiki arguments of the maxima/minimum](https://en.wikipedia.org/wiki/Arg_max)
