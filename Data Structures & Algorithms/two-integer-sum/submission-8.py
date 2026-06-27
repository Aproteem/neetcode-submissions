class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in Map:
                return [Map[remainder], index]
            Map[value] = index
        return 0