# Two Number Sum Prompt
To test your code, run `python3 TwoNumberSum/two_number_sum_test.py`.

## What do you need to solve?
Create a function that takes in two arguments: a non-empty array of unique integers and a target sum integer. If two numbers in the array add up to the target integer, return them in an array in any order. Otherwise, return an empty array. Values cannot be added to themselves and must use a value at a differ index. For example:
```
Input
array = [8, 1, -3, 9, -1, 5]
targetSum = 13
Output
[8, 5] // [5, 8] would also be valid

Input
array = [4, -5, -2, 8, 3]
targetSum = 3
Output
[-5, 8] // [8, -5] would also be valid
```

## Assumptions
- There will be one pair, at most, of numbers in the array that add up to the target.
- The input will be integers. Don't worry about decimals.