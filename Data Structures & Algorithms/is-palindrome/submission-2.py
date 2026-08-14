class Solution:
    def isPalindrome(self, s: str) -> bool:
        l= 0
        r= len(s)-1

        while l<r:
          if self.ignore(s[l]):
            l+=1
          else:
            if self.ignore(s[r]):
              r-=1
            else:
              if s[l].lower() != s[r].lower():
                return False
              else:
                l+=1
                r-=1
        return True

    def ignore(self, c: str):
      c = c.lower()
      
      if (ord(c) - ord("a")) >= 0 and (ord(c) - ord("a")) < 26 :
          #letter
          return False
      else:
          if (ord(c)-ord("0")) >= 0 and (ord(c)-ord("0")) < 9:
            #number
            return False
          else:
            return True