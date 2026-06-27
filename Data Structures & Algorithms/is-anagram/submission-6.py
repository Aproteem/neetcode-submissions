class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        signature = [0 for i in range(26)]

        for c in s:
            signature[ord(c)-(ord("a"))] += 1
            
        for c in t:
            signature[ord(c)-(ord("a"))] -= 1

        for count in signature:
            if count != 0:
                return False
        return True