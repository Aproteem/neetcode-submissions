
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0
        r = len(heights) - 1

        while l != r:
            vol = (r-l) * min( heights[l], heights[r])
            res = max(res, vol)

            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r-1
        return res