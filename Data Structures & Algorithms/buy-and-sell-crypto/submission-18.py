class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        p=[]
        while r<len(prices):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                p.append(profit)
            else:
                l=r
            r+=1
        return max(p,default=0)


