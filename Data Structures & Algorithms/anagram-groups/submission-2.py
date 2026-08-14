from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {strs[0]: []} #key : 'str'  value : [grouped anagrams]

        for string in strs:
            found = False
            for i in temp:
                if self.isAnagram(string, i):
                    temp[i].append(string)
                    found = True
                    break

            if not found:
                temp[string] = [string]
        
        res = []
        for key in  temp:
            res.append(temp[key])

        return res    
    
    
    def isAnagram(self, str1: str, str2: str) -> bool:
        freq_s1 = Counter(str1)
        freq_s2 = Counter(str2)

        if len(freq_s1) != len(freq_s2):
            return False
        else:
            for c in str1:
                if freq_s1[c] != freq_s2[c]:
                    return False
            
        
        return True

        

