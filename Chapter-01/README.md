# Python Objects, Types and Expressions

Objectives of this chapter:-
- Obtain a general working knowledge fo data structure and algorithm
- Understanding core data types and their functions.
- Exploring the object-oriented aspects of the Python Programming Language.

## Understanding DSA

Characteristics of DSA:-
- How algorithm manipulate information contained within data structure.
- How data is arranged in memory.
- What the performance characteristics of particular data structure are.

#### Measuring am algorithm performance involves understanding how each increase in data size affects operations on that data.

## Variable Scope

```python
>>> a = 10
>>> b = 20
>>> def my_function():
...     global a
...     a = 11
...     b = 24
... 
>>> my_function()
>>> a                           # Prints 11
11
>>> b                           # Prints 20
20
```

`global` keyword in python makes the variale globally accesible, so when `my_function()` executed the value of variable `a` changed in global aspect while the value of `b` is just changed in local to `my_functio()` scope, and remains same in global aspect.

 ## Overview of data types and objects

 Python has:-
 - 12 built-in [data types](https://docs.python.org/3/library/stdtypes.html#)
    - 4 numeric type `int`, `float`, `complex`, `bool`.
    - 4 sequence types `str`, `list`, `tuple`, `range`.
    - 1 mapping type `dict`.
    - 2 set type `set`, `frozenset`
    - 1 iterator type

Some more resources can be accessed [here](https://realpython.com/python-data-types/).

#### All data-type in python are objects.

#### Each *object* in python has a **type**, a **value** and an **identity**.

We can get the identity of an object bu using the built-in function `id()`. This returns an identifying integer and on most system this refers to its memory location, although it is not relyable.

```python
>>> a = 42
>>> id(a)
1234567
```

In python there are several ways to compare **objects** in python:-

```python
if a == b:                  # a and b have the same value
```

```python
if a is b:                  # if a and b are the same object
```

```python
if type(a) is type(b):      # a and b are the same type
```

Types of **Objects**:
- **Mutable** :- such as `list` whose value can be changed. They have methods, such as `insert()` or `append()`, that chanes the object value.
- **Im-Mutable** :- such as `strings`, cannot have their value changed, so when we run their methods they simply return a value rather then change the value of underlying object.

## Strings

| Methods | Description |
|--- |--- |
| `s.count(substring, [start, end])` | Counts the occurances of a substring with optional *start* and *end* parameter. |
| `s.expandtabs([tabsize])` | Replace tabs with spaces. |
| `s.find(substring, [start, end])` | Return the index of the first occurance of substring or return -1 if the substring is not found. |
| `s.isalnum()` | Return `True` if all character are alphanumeric, return `False` otherwise. |
| `s.isalpha()` | Return `True` if all character are alphabetic, returns `False` otherwise. |
| `s.isdigit()` | Return `True` if all character are digit, returns `False` otherwise. |
| `s.join(t)` | *Join* the strings in sequence *t*. |
| `s.lower()` | Converts the strings all lowercase. |
| `s.replace(old, new [maxreplace])` | Replace old substring with new substring. |
| `s.strip([character')` | Remove the whitespace or optional characters. |
| `s.split([separator], [maxsplit])` | Splits a string separated by whitespace or an optional separator. Returns a list. |