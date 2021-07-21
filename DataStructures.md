# Built-in Data Structures


```python
import sys
sys.version
```




    '3.9.6 (default, Jun 29 2021, 05:25:02) \n[Clang 12.0.5 (clang-1205.0.22.9)]'



# Dict


```python
a = {"one": 1, "two": 2, "three": 3}
print(type(a))
print(a)
```

    <class 'dict'>
    {'one': 1, 'two': 2, 'three': 3}



```python
for x in a:
    print(x)
```

    one
    two
    three



```python
for x in a.items():
    print(x)
for x, y in a.items():
    print(x, y)
```

    ('one', 1)
    ('two', 2)
    ('three', 3)
    one 1
    two 2
    three 3



```python
for x in a.values():
    print(x)
```

    1
    2
    3



```python
# https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
inverse_mapping = {number: word for word, number in a.items()}
print(type(inverse_mapping))
print(inverse_mapping)
```

    <class 'dict'>
    {1: 'one', 2: 'two', 3: 'three'}



```python
inverse_mapping2 = dict((number, word) for word, number in a.items())
print(type(inverse_mapping2))
print(inverse_mapping2)
```

    <class 'dict'>
    {1: 'one', 2: 'two', 3: 'three'}


# Set


```python
a = [1, 2, 3, 2, 5]
s = set(a)
print(type(s))
print(s)
```

    <class 'set'>
    {1, 2, 3, 5}



```python
s2 = {x for x in a}
print(type(s2))
print(s2)
```

    <class 'set'>
    {1, 2, 3, 5}


# Iteration

## Iterate first k items


```python
a = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
for index, (word, number) in enumerate(a.items()):
    if index >= 3:
        break
    print(word, number)
```

    one 1
    two 2
    three 3

