class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        id1 = [0]*26
        id2 = [0]*26
        for c in s:
            id1[ord(c)-ord('a')] += 1
        for d in t:
            id2[ord(d)-ord('a')] += 1
    
        
        print(id1, '\n', id2)

        if id1 == id2 :
            return True
        else:
            return False
    
