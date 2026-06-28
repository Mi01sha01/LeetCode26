## [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)

## Description

This solution uses **Binary Search** to efficiently find a peak element.

- If the array contains only one element, return index `0`.
- If the first element is greater than the second, the first element is the peak.
- If the last element is greater than the second last, the last element is the peak.
- Otherwise, use Binary Search on the remaining elements.
- If `nums[mid]` is greater than both of its neighbors, return `mid`.
- If the left neighbor is greater than `nums[mid]`, search the left half.
- Otherwise, search the right half.

Since the search space is halved in every iteration, the time complexity is **O(log n)**.

### Complexity

- **Time:** `O(log n)`
- **Space:** `O(1)`