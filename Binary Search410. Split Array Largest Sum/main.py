class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(mid):
            subarrays = 0
            cur_sum = 0
            
            for num in nums:
                cur_sum += num
                if cur_sum > mid:
                    subarrays += 1
                    cur_sum = num
            return  subarrays + 1 <= k
            
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            
            if canSplit(mid):
                r = mid
                 
            else:
                l = mid + 1       

                
        return l   