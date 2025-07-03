# we should check the lengths to see if they match frequencies

# diction ~ freq = {}

# iterate through both list, we'll be using the hash method I believe is the name of it so we store the frequencies of the characters

# return false if a char in t doesnt match

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for char in s:
            freq[char] = 1 + freq.get(char, 0)

        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        
        return True


        
        
        