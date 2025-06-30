class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        freq = {}

        for right, c in enumerate(s):
            freq[c] = 1 + freq.get(c, 0)
            while freq[c] > 1:
                freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length
            



        