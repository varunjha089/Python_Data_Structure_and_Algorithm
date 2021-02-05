# Binary Search

A binary search used to find the elements within list by consistently reducing the amount of data to be searched which increases the rate of finding.

To use `Binary Search` Algorithm, the list must have already sorted.

Basic Python Program for Binary Search:
```python
def binary_search(lists, term):
    SIZE_OF_LIST = len(lists) - 1

    START = 0
    FINISH = SIZE_OF_LIST

    while START <= FINISH:
        MID_POINT = (START + FINISH)
        
        if lists[MID_POINT] == term:
            return MID_POINT
        
        if term > lists[MID_POINT]:
            START = MID_POINT + 1
        else:
            FINISH = MID_POINT - 1

    if START > FINISH:
        return None
```

[Link to .PY file](/Chapter-09/bs_01.py)

To quickely test the programe 
```console
ubuntu@ip:~$ python3 -c "import bs_01 as bs; print(bs.binary_search([1, 5, 6, 9, 8, 12],6))"
```