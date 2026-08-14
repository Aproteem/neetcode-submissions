class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        result = [1]

        for i in range(len(nums)-1):
            pre *= nums[i]
            result.append(pre)
        suf = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suf
            suf *= nums[i]

        return result

        