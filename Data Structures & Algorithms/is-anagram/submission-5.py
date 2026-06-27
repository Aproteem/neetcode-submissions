class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        signature_s = [0 for i in range(26)]
        signature_t = [0 for i in range(26)]

        for c in s:
            signature_s[ord(c)-(ord("a"))] += 1
            
        for c in t:
            signature_t[ord(c)-(ord("a"))] += 1

        print(signature_s)
        return signature_s == signature_t
