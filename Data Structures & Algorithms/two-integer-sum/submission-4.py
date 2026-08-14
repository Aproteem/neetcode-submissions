class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionery = {} # number : index
        # for index, number in enumerate(nums):
        #     dictionery[number] = index
        #     b = target - number
        #     if b in dictionery and dictionery.get(b)  != index :
        #         return [dictionery.get(b), index]
        # return []
        prevmap = {}    # value : index
        for index, number in enumerate(nums):
            diff = target - number
            if diff in prevmap:
                return [prevmap[diff], index]
            
            prevmap[number] = index

        return []
