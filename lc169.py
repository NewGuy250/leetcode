# O(n) Time Complexity, single traversal through the array
# O(1) Space complexity, no additional data structures

class Solution:
    def majorityElement(self, nums):
        # Get current number and counter
        curr, count = None, 0
        # Iterate
        for num in nums:
            # Assign curr if 0
            if count == 0:
                curr = num
            # Increment or decrement
            count += 1 if num == curr else -1
        return curr