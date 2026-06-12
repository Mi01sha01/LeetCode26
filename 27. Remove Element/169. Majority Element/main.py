class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        # Iterate through each number in the array
        for i in nums:

            # If there is no current candidate,
            # choose the current number as the new candidate
            if count == 0:
                candidate = i
                count += 1

            # If the current number matches the candidate,
            # increase the vote count
            elif i == candidate:
                count += 1

            # If the current number is different,
            # cancel out one vote
            else:
                count -= 1

        # The remaining candidate is the majority element
        return candidate
