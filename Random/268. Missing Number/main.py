class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        sum_n = (n * (n + 1))//2
        for num in nums:
            sum_n -= num
            
            
            
        return sum_n