# O(n) Time, because it iterates through each element once
# O(n) Space, becase it can store n elements in the dict
class Solution(object):
    def twoSum(self, nums, target):
        seen = dict() # Get seen numbers and their index
        for i, n in enumerate(nums):
            complement = target - n # Find complement
            if complement in seen: # If in seen, return
                return [seen[complement], i]
            seen[n] = i

