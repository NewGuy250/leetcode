# O(n) Time, because the number of digits is proportional to log(number)
# O(n) Space, becase the storage is constant
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check edge cases such as Negative and numbers ending in 0 except 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # Initialize Variable to store reversed second half of num
        reversed_half = 0
        # Reverse the digits of the second half of num
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10 # Add last digit to varaible
            x //=10 # Remove last digit
        return x == reversed_half or x == reversed_half // 10 # Check if 1st half matches 2nd half
