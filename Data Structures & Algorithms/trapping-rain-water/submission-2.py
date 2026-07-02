class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxwater = 0
        # while l<r:#pointers point to two extreme heights, or l>r
        #     if height[l+1] > height[l]:
        #         l+=1
        #     if height[r-1] > height[r]:
        #         r-=1
        #     if  (height[r-1] < height [r]) and (height[l+1] < height [l]) :
        #         break

        if l>=r:
            return 0
        else:
            while l<r:
                #prober switch mechanism
                if height[l]<=height[r]:
                    prober = l+1
                    leftprober = True
                else:
                    prober = r-1
                    leftprober = False
                ##use booleon to switch probing left or right
                if(leftprober):
                    while height[prober] < height[l] and prober<r:
                        maxwater += height[l] - height[prober]
                        prober += 1
                    l = prober
                else:
                    while height[prober] < height[r] and prober>l:
                        maxwater += height[r] - height[prober]
                        prober -= 1
                    r = prober
            
            return maxwater