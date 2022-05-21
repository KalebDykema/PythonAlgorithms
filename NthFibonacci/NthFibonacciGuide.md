# Nth Fibonacci Guide

## Solution One
### Simplified Complexity
O(2^2) time | O(n) space

### Full Complexity
O(2^(n-2)) time | O(n-1) space

### Time Complexity Visualization
O(2^(6-2)) = 16 items on bottom row
The X's never get run and are only used to calculate the max complexity.
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
   2   1   X   X     X   X   X   X X   X   X   X     X   X   X   X
```

### Space Complexity Visualization
O(6-1) = 5 items max on the stack at a time
```
  2  ->  1
  ^      ^
  3      3  ->  2             2  ->  1
  ^      ^      ^             ^      ^
  4      4      4  ->  3      3      3  ->  2
  ^      ^      ^      ^      ^      ^      ^
  5      5      5      5  ->  4      4      4
  ^      ^      ^      ^      ^      ^      ^
  6      6      6      6      6      6      6
```