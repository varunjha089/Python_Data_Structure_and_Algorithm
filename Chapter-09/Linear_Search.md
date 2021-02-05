# Linear Search

A python list look's basically like this.

| 60 | 1 | 88 | 10 | 11 | 100 |
|---|---|---|---|---|---|
|[0] | [1] | [2] | [3] | [4] | [5] |


## Unordered Linear Search

Basic Python Program for linear search:

```python
def search(lists, term):
    for i in range(len(lists)):
        if term == lists[i]:
            return i
    return 0
```

In above program the `search()` function takes two parameter:
- `lists` :- A list data type object.
- `term` :- The term we are looking for, in the array. Also called **search term**.

We uses `len(lists)` to determine the size of array. And `term` tells us the term we want to find in the `lists` arrar.

### The **`Unordered Linear Search`** has word case running time of **`O(N)`**

## Ordered Linear Search

