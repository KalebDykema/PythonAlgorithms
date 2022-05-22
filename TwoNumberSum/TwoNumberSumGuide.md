# Two Number Sum Guide

## Solution One
### Simplified Complexity
O(n^2) time | O(1) space

### Full Complexity
O(n^2) time | O(1) space

### Time Complexity
O(4^2) = 16 total loops
The sample array in this case is [4, 6, 1, -3], and the target is -5. The expected result is an empty array, meaning we need to loop through the full length.
```
    4 => 4 -> 6 -> 1 -> -3
    6 => 4 -> 6 -> 1 -> -3
    1 => 4 -> 6 -> 1 -> -3
   -3 => 4 -> 6 -> 1 -> -3
```

### Space Complexity
O(1)
While there are various items stored on the stack, it is constant no matter how much the input grows or shrinks.

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
O(n-1) time | O(3) space

### Time Complexity
O(6-1) = 5 items looped through
```
  Index
  2 -> 3 -> 4 -> 5 -> 6
  Value
  1 -> 1 -> 2 -> 3 -> 5
```

## Space Complexity Visualizaiton
O(3) = 3 items stored on stack
Since we only overwrite the current slots in the area, we only use 3 spots in memory: 2 for the array itself, and 1 for the returned number.