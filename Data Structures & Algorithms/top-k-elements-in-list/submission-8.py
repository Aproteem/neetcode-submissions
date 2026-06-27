from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #used defaultdict properply, we use it when we know we are gonna search a key in dictonary that wont be there
        #and is required to be initialized. 

        #time complexity O(nlogn) sorting used...SELF IDEA
        
        frequency = defaultdict(int)
        for i in nums:
            frequency[i] += 1

        frequency_list = []
        for value, count in frequency.items():
            frequency_list.append([count, value])

        #utilizing bucket sort
        freqTable = [[] for i in range (len(nums))]
        for item in frequency_list:
            freqTable[item[0]-1].append(item[1])
        
        res = []
        for i in range(len(freqTable)-1, -1, -1):
            if freqTable[i] == []:
                continue
            else:
                for j in freqTable[i]:
                    res.append(j)
                    if len(res) == k:
                        break
            if len(res) == k:
                break
        
        return res


        '''
        res = []
        for i in range(len(frequency_list)-1, len(frequency_list)-(k+1), -1):
            res.append(sorted_freqList[i][1])
        
        return res
        '''
    


