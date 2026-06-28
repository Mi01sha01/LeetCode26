#$ [268. Missing Number](https://leetcode.com/problems/missing-number/)

## Description

This solution uses the **sum formula** to find the missing number.

- Calculate the expected sum of numbers from `0` to `n` using:
  \[
  \frac{n(n+1)}{2}
  \]
- Subtract every number in the array from this expected sum.
- The remaining value is the missing number.

### Time Complexity
- **O(n)**

### Space Complexity
- **O(1)**