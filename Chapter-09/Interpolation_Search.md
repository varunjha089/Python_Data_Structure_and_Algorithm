# Interpolation Search

It is another varient of **`Binary Search`**

Let's look at the following example:-

| Array -> | 44 | 60 | 75 | 100 | 120 | 230 | 250 |
|---|---|---|---|---|---|---|---|
| Index Number -> |[0] | [1] | [2] | [3] | [4] | [5] | [6] |


Let's find 120, in it.

First find mid-point of this array.

```python
def nearest_mid(lists, start, end, value):
    return start + (( end - start) / (lists[end] - lists[start] )) * ( value - lists[start])
```

[link to .PY file](/Chapter-09/is.py)

To quickely test the programe 
```console
ubuntu@ip:~$ python3 -c "import is_01 as ise; print(ise.nearest_mid([0, 4, 5, 12, 43, 54, 60], 0, 6, 54))"
```

In **`Binary Search`**, the pointer is exactly in the **`middle`**, whereas in **`Interpolation Search`**, our pointer is swayed more to left or right. This is caused be the effect of the multiplier used when dividing to obtain the midpoint.

```python
from is_01 import *

def interpolation_search(lists, term):
    size = len(lists) - 1

    start = 0
    end = size

    while start < end:
        mid_point = nearest_mid(lists, start, end, term)

        if mid_point > end or mid_point < start:
            return None

        if lists[mid_point] == term:
            start = mid_point + 1
        else:
            end = mid_point - 1
        
        if start > end:
            return None
```

[Link to .PY file](/Chapter-09/is_02.py)