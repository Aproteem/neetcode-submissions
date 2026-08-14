class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0 for i in range(len(nums))]
        pre = []
        prod = 1
        for i in range(len(nums)):
            pre.append(prod)
            prod *= nums[i]
        
        pst = [0 for i in range(len(nums))]
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            pst[i] = prod
            prod *= nums[i]

        for i in range(len(nums)):
            output[i] = pre[i] * pst[i]
        
        return output


