from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) 
        
        #default dict assigns an empty string when no key is found

        for string in strs:
            key = self.identity(string)
            group[key].append(string)

        return list(group.values())


    
    def identity(self, string: str) -> tuple:
        res = [0]*26
        for c in string:
            index = ord(c)-ord('a') #constraint input string is all lowercase alphabet
            res[index] += 1
        
        return tuple(res)

   
'''    
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
'''
        

