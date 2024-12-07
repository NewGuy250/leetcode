# O(n) Time Complexity, it iterates through each number
# O(n) Space complexity
class Solution:
    def longestConsecutive(self, nums):
        # Set to remove duplicates
        s = set(nums)

        # Keep track of longest seq
        longest = 0

        # Iterate for each number
        for num in s:
            # Find start
            if num - 1 not in s:
                curr = 1
                while num + 1 in s:
                    curr += 1
                    num += 1
                # Find if curr is the longest
                longest = max(longest, curr)

        return longest