# O(n) Time Complexity, iterates over each num
# O(1) Space complexity

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate over the digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            
            # Verify number isn't going to become 10
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            # If 10 set to 0
            digits[i] = 0

            # If at 0 index and 10, add 1 to the beginning
            if i == 0:
                return [1] + digits
