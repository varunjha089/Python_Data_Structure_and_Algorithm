# Searching

One of the important use of `Searching` is `sorting`. It is just impossible to sort without some variant of a search operation.

There are two types of `Searching` Algorithm.
- [Linear Search](/Chapter-09/Linear_Search.md)
- [Binary Search](/Chapter-09/Binary_Search.md)
    - [Interpolation Search](/Chapter-09/Interpolation_Search.md)

## Choosing a search Algorithm

**`Binary Search`** operation are better at performance than **`Linear Search`**, because of the ***sequential probing*** of elements in the list to find the search term, **`Linear Search`** have a time complexity of **`O(N)`**. Which results in very poor performance when the list is large.

The **`Binary Search`** operation on the other side, divide the lists into two, when a search is attempted. The time complexity of **`Binary Search`** is **`O(Log N)`**. Despite the speed in using **`Binary Search`**, it cann't be used on an unsorted list of items.

Whereas **`Interpolation Search`** algorithm the mid is calculated for which gives higher probability of obtaining our search term. The time complexity of **`Interpolation Search`** is **`O(Log (Log N))`**, which gives raise to faster search then it's varient **`Binary Search`**.