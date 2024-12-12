# O(n) Time, iterates through each word
# O(n) Space, words variable

class Solution:
    def reverseWords(self, s):
        words = s.split()
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)