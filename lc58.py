# O(n) Time Complexity, because it can go through all the characters
# O(1) Space Complexity, fixed space
class Solution:
    def lengthOfLastWord(self, s):
        # Initialize end and accumulator
        i, length = len(s) - 1, 0
        
        # Get rid of white space
        while s[i] == " ":
            i -= 1
        # Count last word
        while i >= 0 and s[i] != " ":
            length += 1

        return length