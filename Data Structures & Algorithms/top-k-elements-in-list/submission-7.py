from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for i in nums:
            frequency[i] += 1

        frequency_list = []
        for value, count in frequency.items():
            frequency_list.append([count, value])

        sorted_freqList = sorted(frequency_list)

        res = []
        for i in range(len(frequency_list)-1, len(frequency_list)-(k+1), -1):
            res.append(sorted_freqList[i][1])
        
        return res