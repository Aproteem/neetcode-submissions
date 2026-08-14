class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionery = {} # index : number
        for index, number in enumerate(nums):
            b = target - number
            if b in dictionery and dictionery.get(b)  != index :
                return [dictionery[b], index]
            dictionery[number] = index