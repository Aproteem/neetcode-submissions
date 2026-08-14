class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) != 0):  
            l, r = 0, 0
            maxl = 0
            sub = set()

            while r < len(s):
                if s[r] in sub:
                    sub.remove(s[l])
                    l += 1
                else:
                    sub.add(s[r])
                    r += 1
                    maxl = max(maxl, len(sub))
            return maxl
        else:
            return 0    
