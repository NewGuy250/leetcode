# O(n) Time complexity, since we have to slice the nums and every element must be reupdated
# O(1) Space complexity, since its done in place

class Solution:
    def rotate(self, nums, k):
        # Reduce k if too large
        k = k % len(nums)
        # Change nums in place
        nums[:] = nums[-k:] + nums[:-k]
