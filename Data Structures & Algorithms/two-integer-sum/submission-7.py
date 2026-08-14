class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # key : value
        for i, num in enumerate(nums):
           hashmap[num] = i

        for i, num in enumerate(nums):
            search = target - num
            if search in hashmap and hashmap[search] != i:
                return [i, hashmap[search]]
        
        return []