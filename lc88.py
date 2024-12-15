# O(m + n) Time Complexity, because it can go through all the characters for each arr
# O(1) Space Complexity, fixed space

class Solution:
    def merge(self, nums1, m, nums2, n):
        # Get right pointer of nums1
        last = m + n - 1 

        # Merge arrays in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else: 
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        # Merge any leftover
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1