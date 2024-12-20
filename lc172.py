# O(log5(n)) Time, because loop runs approximately log5(n) times, as n is divided by 5 in each iteration
# O(1) Space

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0  # Initialize the count of trailing zeroes
        
        # Count factors of 5 in n!
        while n >= 5:
            n //= 5  # Divide n by 5 to count the multiples of 5
            count += n  # Add the count of multiples of 5 to the result
        
        return count  # Return the total count of trailing zeroes
