class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1

            if(nums[i]>0):
                #in sorted if my current number is positive,
                #all numbers after it is positve, can never add to 0
                break

            target = -(nums[i])
            while l<r:
                if nums[l]+nums[r] == target:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                elif nums[l]+nums[r] > target:
                    r -= 1
                elif nums[l]+nums[r] < target:
                    l += 1

        res = set(res)
        for item in res:
            item = list(item)
        

        return list(res)