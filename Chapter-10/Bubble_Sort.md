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



