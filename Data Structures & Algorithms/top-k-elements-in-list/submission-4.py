
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [ [] for i in range (len(nums))]
        #a list of lists, [[1,2],[0],[4]] (indices + 1) are frequencies 
        #so 1 and 2 are once, 0 is twice 4 is three times
        
        temp = dict(Counter(nums))
        freq = []
        for i in temp:
            freq.append([temp[i], i])
        # freq is a list with pairs [frequency, numbers

        for pair in freq:
            buckets[pair[0]-1].append(pair[1])
        #buckets now have each number at their frequency list
        print(buckets)
        
        index = len(buckets)-1
        res = []
        while index >= 0 and len(res) < k:
            if buckets[index] == []:
                index -= 1
            else:
                for i in buckets[index]:
                    res.append(i)
                    if len(res) == k:
                        break
                index -= 1

        return res
    




        

        