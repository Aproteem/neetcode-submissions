class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Grouped = {}

        for word in strs:
            sig = [0 for i in range(26)]
            for c in word:
                sig[ord(c)-ord("a")] += 1
            key = tuple(sig)
            if key in Grouped:
                Grouped[key].append(word)
            else:
                Grouped[key] = [word]
        
        return ( list(Grouped.values()) )