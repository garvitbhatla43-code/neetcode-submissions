class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        p=[]
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            p.append(area)
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return max(p)
        