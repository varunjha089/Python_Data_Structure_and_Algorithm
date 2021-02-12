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

<iframe
  src="https://carbon.now.sh/embed?bg=rgba%28171%2C+184%2C+195%2C+1%29&t=seti&wt=none&l=python&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=19px&ph=22px&ln=true&fl=1&fm=Hack&fs=16.5px&lh=176%25&si=false&es=2x&wm=false&code=def%2520bubble%28lists%29%253A%250A%2520%2520%2520%2520iterationNumber%2520%253D%2520len%28lists%29%2520-%25201%250A%2520%2520%2520%2520for%2520i%2520in%2520range%28iterationNumber%29%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520for%2520j%2520in%2520range%28iterationNumber%29%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520if%2520lists%255Bj%255D%2520%253E%2520lists%255Bj%2520%252B%25201%255D%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520temp%2520%253D%2520lists%255Bj%255D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520lists%255Bj%255D%2520%253D%2520lists%255Bj%2520%252B%25201%255D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520lists%255Bj%2520%252B%25201%255D%2520%253D%2520temp"
  style="width: 509px; height: 342px; border:0; transform: scale(1); overflow:hidden;"
  sandbox="allow-scripts allow-same-origin">
</iframe>

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