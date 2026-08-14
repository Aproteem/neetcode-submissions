class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key = number : value = count
        freq = [[] for i in range (len(nums))] # a freq of a item in nums cannot be 0 or > max length of num
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for value, f in count.items() :
            freq[f-1].append(value)

        for i in  range(len(freq)-1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k :
                    return res
