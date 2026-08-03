class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1 

        maxP = 0
    
        while r < len(prices):
            price = prices[r] - prices[l]
            if  price > 0:
                maxP = max(maxP, price)
            else:
                l = r
            r += 1
        return maxP
        
        