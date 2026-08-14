class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        longest = 0

        for num in set_num:
            #only concern ourselves if elements that are a start of a sequence
            length = 0  #tallies current seq len

            while (num - 1) not in set_num: 
                if (num+length) in set_num:
                    length += 1 #sequencially checks for  + 1 numbers
                else:
                    break
                    
            if (length > longest):
                longest = length
    
        return longest



