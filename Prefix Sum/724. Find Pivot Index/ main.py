class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefSum = 0
        totalSum = sum(nums) 
       
        for pivot in range(len(nums)):
            sufSum = totalSum - nums[pivot] - prefSum 
            if prefSum == sufSum:
                return pivot 
            prefSum += nums[pivot]    
        return -1 
      
      
      
 