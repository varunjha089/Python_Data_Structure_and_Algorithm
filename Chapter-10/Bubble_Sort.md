# Bubble Sort

Take this list as an example 

| Number -> | 5 | 2 |
|---|---|---|
| Index -> | [0] | [1] |

In **`Bubble Sort`** we compart adjacent elements in the list and swap them in right order. To sort the above list, simply swap them into right position with **2** occuping index **0**, and **5** occuping index **1**.

| Number -> | 2 | 5 |
|---|---|---|
| Index -> | [0] | [1] |

To do so we need to create a temporary storage area.
             
       Temporary Storage Area    
                 |
                \./    
                 _
                [_]
               /   \
              /     \
             /       \
            [5       2]
             \       /
              \     /
               \   /
                \ /
                 @




Check the source file [here](/Chapter-10/bubbleSort.py).

![Bubble Sort](/Chapter-10/assets/bubbleSort01.png)

* This file has been created using [https://carbon.now.sh](https://carbon.now.sh/).

In this code file 
- Line 6-8 :
       - first element **5** will be copied to a temporary location, **`temp`**. Then element **2** will be moved to index **0**. And, finnaly **5** will be moved to index **1**.

- The entire code has been running in double nested loop.
       
       - The first loop is from line **4 to 8**.
       
       - The second loop is from line **3 to 8**.

Knowing how many times to swap is important in **`Bubble Sort`** algorithm.

Let's take a list :- [ 3, 2, 1 ]

| [ 3, | 2, | 1 ] | |
|---|---|---|---|
| \ | / | | |
| / | \ | | |
| [ 2, | 3, | 1 ] | Swap 1 |
| | \ | / | |
| | / | \ | |
| [ 2, | 1, | 3 ] | Swap 2 |

The **`if`** statement at **line 5** makes sure no needless swap occurs. The inner **`for`** loop at **line 4** only causes the swapping of adjacent elements to occur exactly twice in our list.

An outer **`for`** loop at **line 3** cause the entire process to occur again. So now our sorting will be like 

| [ 2, | 1, | 3 ] | |
|---|---|---|---|
| \ | / | | |
| / | \ | | |
| [ 1, | 2, | 3 ] | Swap 1 |
| | !_ | _! | |
| | No | swap | |
| [ 1, | 2, | 3 ] |  |


From this we can conclude that the total amount of 4 comparisions is needed to sort the list. So, both loop has to run **`len(lists) - 1`** times for all elements to be sorted.

**Bubble Sort** is highly inefficient sorting algorithm whith time complexity of **`O(N2)`**, and best case of **`O(N)`**. So, it is not recommended to sort a large list.