class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        seq = [] # will contain all sequences

        for i in nums:
            if i-1 not in uniq:
                temp = [i]
                j=i+1
                while j in uniq:
                    temp.append(j)
                    j += 1
                seq.append(temp)
        maxlen = 0
        for sequence in seq:
            maxlen = max(maxlen, len(sequence))
            
        return maxlen
