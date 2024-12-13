# O(n) time complexity, iterates through each number
#O(1) space complexity, stores k only

class Solution:
    def removeElement(self, nums, val):
        # Get counter/pointer
        k = 0

        for num in nums:
            # Increment and replace index if != val
            if num != val:
                nums[k] = num
                k += 1
        return k