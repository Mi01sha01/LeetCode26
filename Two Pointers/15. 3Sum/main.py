class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue 
            
            l, r = i + 1, n - 1   
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and  nums[l - 1] == nums[l]:
                            l += 1
        return result                    
                            
             
             #[-4, -1, -1, 0, 1, 2]               
                        
            
                