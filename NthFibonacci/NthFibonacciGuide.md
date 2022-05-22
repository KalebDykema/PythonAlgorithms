# Nth Fibonacci Guide

## Solution One
### Simplified Complexity
O(2^n) time | O(n) space

### Full Complexity
O(2^(n-2)) time | O(n-1) space

### Time Complexity
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

   2 becomes 1 and 1 becomes 0. Adding up all of the 2's after equating them to 1 comes out to 5.
```

### Space Complexity
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

  NOTE: The actual values above are just the indexes, not the fibonacci values.
```

## Solution Two
### Simplified Complexity
O(n) time | O(n) space

### Full Complexity
O(n-1) time | O(n-1) space

### Time Complexity
O(6-1) = 5 items looped through
```
  5 <= 3 +  2 <= 1 +  1
  6 -> 5 -> 4 -> 3 -> 2 (memoized)
     \
      4 (already memoized, stop here)

  Essentially, we get the 6th index by adding up all of the previous fibonacci numbers after going down to the smallest index that is already memoized and memoizing the rest back up.
```

### Space Complexity
O(6-1) = 5 items max on the stack at a time
```
  2
  ^
  3
  ^
  4
  ^
  5
  ^
  6

  NOTE: The actual values above are just the indexes, not the fibonacci values.
```

## Solution Three
### Simplified Complexity
O(n) time | O(1) space

### Full Complexity
O(n-1) time | O(1) space

### Time Complexity
O(6-1) = 5 items looped through
```
  Index
  2 -> 3 -> 4 -> 5 -> 6
  Value
  1 -> 1 -> 2 -> 3 -> 5
```

## Space Complexity
O(1)
While there are various items stored on the stack, it is constant no matter how much the input grows or shrinks.