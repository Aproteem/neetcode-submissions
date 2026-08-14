class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # j is left and k is right
            j, k = i+1, len(nums) - 1

            if i>0 and num == nums[i-1]:
                continue

            while j<k:
                
                threesum = num + nums[j] + nums[k] 

                if threesum < 0:
                    j += 1
                elif threesum > 0:
                    k-=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while  nums[j] == nums[j-1] and j<k:
                        j+=1


        return res