class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge case
        if x == 0:
            return 0
        
        # Initialize the binary search range.
        # first is lower bound, last is upper bound
        first, last = 1, x
        
        # Perform binary search to find the integer square root.
        while first <= last:
            # Calculate the middle of the current range.
            mid = first + (last - first) // 2
            
            # Check if mid is right number
            if mid == x // mid:
                return mid
            
            # If mid is greater, search left half
            elif mid > x // mid:
                last = mid - 1
            
            # Else search right
            else:
                first = mid + 1
        
        # Return if no sqrt found
        return last
