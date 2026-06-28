## [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Description

This solution uses **Binary Search** twice:

- The first binary search finds the **first occurrence** of the target by continuing the search on the left after finding the target.
- The second binary search finds the **last occurrence** of the target by continuing the search on the right after finding the target.
- If the target does not exist, both searches return `-1`.

### Time Complexity

- **O(log n)**

### Space Complexity

- **O(1)**