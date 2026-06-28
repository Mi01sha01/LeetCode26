## [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

## Description

This solution uses **Binary Search** to efficiently find the first bad version.

- Initialize two pointers: `left = 1` and `right = n`.
- Find the middle version using `mid = (left + right) // 2`.
- If `mid` is a bad version, the first bad version is either `mid` or to its left, so move the right pointer to `mid`.
- Otherwise, the first bad version must be to the right, so move the left pointer to `mid + 1`.
- Continue until both pointers meet. The meeting point is the first bad version.

## Complexity

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`