# Nth Fibonacci Guide

## Solution One
### Simplified Complexity
O(2^2) time | O(n) space

### Full Complexity
O(2^(n-2)) time | O(n) space

### Time Complexity Visualization
O(2^(6-2)) = 16
```
                                  6
                   _______________|_______________
                  |                               |
                  5                               4
          ________|________               ________|________
         |                 |             |                 |
         4                 3             3                 2
      ___|___           ___|___       ___|___           ___|___
     |       |         |       |     |       |         |       |
     3       2         2       1     2       1         X       X
    / \     / \       / \     / \   / \     / \       / \     / \ 
   2   1   X  X      X   X   X   X X   X   X   X     X   X   X   X (16 items)
```