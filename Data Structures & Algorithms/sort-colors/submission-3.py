class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count= [0,0,0]

        for i in nums:
            count[i] += 1
        #we have a freq array at count
        index = 0
        for color in range(3):
            while count[color] != 0:
                nums[index] = color
                count[color] -= 1
                index += 1



            

        