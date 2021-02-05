# Linear Search

A python list look's basically like this.

| Array -> | 60 | 1 | 88 | 10 | 11 | 100 |
|---|---|---|---|---|---|---|
| Index Number -> |[0] | [1] | [2] | [3] | [4] | [5] |


## Unordered Linear Search

Basic Python Program for Unordered linear search:

```python
def search(lists, term):
    for i in range(len(lists)):
        if term == lists[i]:
            return i
    return 0
```

[Link to .PY file](/Chapter-09/ls_01.py)


In above program the `search()` function takes two parameter:
- `lists` :- A list data type object.
- `term` :- The term we are looking for, in the array. Also called **search term**.

We uses `len(lists)` to determine the size of array. And `term` tells us the term we want to find in the `lists` arrar.

### The **`Unordered Linear Search`** has worst case running time of **`O(N)`**.

## Ordered Linear Search

The `Algorithm` can be :-
1. Sort the list
2. Move through the list sequentially
3. If the `Search` item is greater than the item currently under inspection in the loop, then quit and return `None`.

Basic Python Program for Ordered linear search:

```python
def search(lists, term):
    for i in range(len(lists)):
        if term == lists[i]:
            return i
        elif lists[i] > term:
            return None
    return None
```

[Link to .PY file](/chapter-09/ls_02.py)

#### The time complexity of **`Ordered Linear Search`** is **`O(N)`**.
