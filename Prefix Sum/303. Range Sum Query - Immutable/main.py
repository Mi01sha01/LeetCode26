from itertools import accumulate
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefixSum[right] - self.prefixSum[left - 1]
        return self.prefixSum[right]