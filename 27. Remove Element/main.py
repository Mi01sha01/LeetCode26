from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 'slow' points to the position where the next
        # element that is not equal to 'val' should be placed.
        slow = 0

        # 'fast' traverses the entire array.
        for fast in range(len(nums)):
            
            # If the current element is not the value to remove,
            # keep it in the array.
            if nums[fast] != val:
                
                # Place the valid element at the 'slow' index.
                nums[slow] = nums[fast]
                
                # Move 'slow' to the next available position.
                slow += 1

        # 'slow' represents the number of elements
        # that are not equal to 'val'.
        return slow
