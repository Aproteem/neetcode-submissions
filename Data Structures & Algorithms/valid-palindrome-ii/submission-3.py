class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome (l:int,r:int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        
        l,r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            elif checkPalindrome(l+1,r):
                return True
            elif checkPalindrome(l,r-1):
                return True
            else:
                return False
        return True


        
        