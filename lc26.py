# O(n) Time Complexity, iterate through each element
# O(n) Space Complexity, len of nums can be seen

class Solution:
    def removeDuplicates(self, nums):
        k = 0
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[k] = num
                k += 1
        return k