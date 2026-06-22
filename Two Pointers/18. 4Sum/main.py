class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                     
                l, r = j + 1, n - 1
                while l < r:
                    current_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if current_sum > target:
                        r -= 1
                    elif current_sum < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])   
                        l += 1
                        r -= 1
                        # Skip duplicate values for the third and fourth numbers
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                            
        return res