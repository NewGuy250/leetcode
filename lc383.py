# O(m + n) Time Complexity, must iterate through each letter in each str
# O(1) Space Complexity

class Solution:
    def canConstruct(self, ransomNote, magazine):
        # Keep track of letters
        maga_hash = {}
        # Fill Hashmap
        for c in magazine:
            maga_hash[c] = 1 + maga_hash.get(c, 0)
        # Decrement Hashmap and Validate
        for c in ransomNote:
            if c not in maga_hash or maga_hash[c] <= 0:
                return False
            maga_hash[c] -= 1
        
        return True