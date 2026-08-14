class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}    # value : index
        for index, number in enumerate(nums):
            diff = target - number
            if diff in prevmap:
                return [prevmap[diff], index]
            
            prevmap[number] = index

        return []