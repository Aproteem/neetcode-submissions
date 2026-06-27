class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for i in range (len(nums))]
        right = [1 for i in range (len(nums))]
        res = []
        for i in range(1,len(nums),1):
            left[i] = left[i-1] * nums[i-1]
        print(left)

        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1]*right[i+1]
        print(right)

        for i in range(len(nums)):
            res.append( left[i] * right [i])
        
        return res