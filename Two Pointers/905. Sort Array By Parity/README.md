## [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)

## Approach
Use two pointers:
- Left pointer searches for odd numbers.
- Right pointer searches for even numbers.
- Swap when an odd number is found on the left and an even number is found on the right.

### Complexity
- Time: O(n)
- Space: O(1)