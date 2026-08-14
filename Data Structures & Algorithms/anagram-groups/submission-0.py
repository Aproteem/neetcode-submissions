class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # key = char count array : value = list of the strings 
       

        for string in strs:
            chr_count = [0]*26  # for a ... z 
            for c in string:
                chr_count[ord(c)-ord("a")] += 1
            
            res[tuple(chr_count)].append(string)
        
        return list(res.values())
