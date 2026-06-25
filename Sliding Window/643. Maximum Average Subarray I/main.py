class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxSum = curSum

        l, r = 0, k
        while r < len(nums):
            curSum += nums[r] - nums[l]
            maxSum = max(maxSum, curSum)
            l += 1
            r += 1

        return maxSum / k