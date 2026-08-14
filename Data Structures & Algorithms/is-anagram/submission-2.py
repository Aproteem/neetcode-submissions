class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {} #key = char, val = count

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        for c in t:
            if c in freq:
                freq[c] -= 1
            else:
                return False
        
        for c in freq:
            if freq[c] != 0:
                return False
        
        return True

