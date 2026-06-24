class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur_sum = 0
        min_len = float('inf')
        
        for r in range(len(nums)):
            cur_sum += nums[r]
            
            while cur_sum >= target:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        
        if min_len == float('inf'):
            return 0
        return min_len   
                
        
        
             