class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)

        sequence = defaultdict(list)

        for number in nums:
            if (number - 1) in lookup:
                continue
                #not a start of sequence
            else:
                sequence[number]
        
        for key in list(sequence.keys()):
            curr = key
            nxt = curr + 1
            while nxt in lookup:
                sequence[key].append(curr)
                curr += 1
                nxt = curr + 1
            sequence[key].append(curr)

        maxlen = 0
        for values in list(sequence.values()):
            maxlen = max (maxlen, len(values))

        return maxlen