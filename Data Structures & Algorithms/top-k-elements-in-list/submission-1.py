
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency list
        freq = dict(Counter(nums))
        freq_sort = []

        #flipped frequence and numbers
        for i in freq:
            freq_sort.append([freq[i], i]) #[freq, number]
        
        #sorted on basis of frequency
        freq_sort.sort(reverse=True)
        
        res = []

        for i in range(k):
            res.append(freq_sort[i][1])
        
        return res



        

        