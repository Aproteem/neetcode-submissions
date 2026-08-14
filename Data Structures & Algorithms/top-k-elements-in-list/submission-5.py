from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_freq = [[] for i  in range(len(nums))]
        freq = dict(Counter(nums))
        res = []

        for num, count in freq.items():
            sorted_freq[count-1].append(num)
        
        for i in range(len(sorted_freq)-1,-1,-1):
            if sorted_freq[i] == []:
                continue
            else:
                for j in sorted_freq[i]:
                    res.append(j)
                    if len(res) == k:
                        break

            if len(res) == k:
                        break 
                        
        return res






        