class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup = set(nums)
        if len(nodup) == len(nums):
            return False
        else:
            return True