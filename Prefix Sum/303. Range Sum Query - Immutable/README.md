## [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

## Description

This solution uses a **Prefix Sum** array to answer range sum queries efficiently.

- Build a prefix sum array during initialization.
- Each query is answered using the difference of two prefix sums.
- If `left` is `0`, simply return the prefix sum at `right`.

### Time Complexity

- **Initialization:** `O(n)`
- **sumRange():** `O(1)`

### Space Complexity

- **O(n)**